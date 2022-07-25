from templateframework.metadata import Metadata

def run(metadata: Metadata = None):

    import os
    
    def limpar_arquivos_temporarios():
        if os.path.isdir('spooned'):
            import shutil
            shutil.rmtree('spooned')

    target_project = str(metadata.target_path)

    home = os.path.expanduser('~')
    dir_cdd_jar = home + "/.stk/stacks/dev-java/cdd/cdd.jar"
    
    comando_java = ["java", "-jar", dir_cdd_jar, "-p", target_project]

    import subprocess
    result = subprocess.run(comando_java,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True)

    if result.stderr == "":
        print(result.stderr)
    else:
        for item in result.stdout.split("\n"):
            print(item)

        limpar_arquivos_temporarios()
            
    return metadata