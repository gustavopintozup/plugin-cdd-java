import os
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    
    def encontar_jar_cdd():
        import glob
        home = os.path.expanduser('~')

        for file in glob.glob(home + "/.stk/stacks/*/plugin-cdd-java/cdd.jar"):
            return os.path.abspath(file)
            
    def limpar_arquivos_temporarios():
        if os.path.isdir('spooned'):
            import shutil
            shutil.rmtree('spooned')

    target_project = str(metadata.target_path)
    dir_cdd_jar = encontar_jar_cdd()
    
    comando_java = ["java", "-jar", dir_cdd_jar, "-p", target_project]

    import subprocess
    result = subprocess.run(comando_java,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True)

    if result.returncode == 0:
        for item in result.stdout.split("\n"):
            print(item)
    else:
        for item in result.stderr.split("\n"):
            print(item)
        
    limpar_arquivos_temporarios()
            
    return metadata