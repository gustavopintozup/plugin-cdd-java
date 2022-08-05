import os, sys
from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    def encontar_jar_cdd():
        import glob
        home = os.path.expanduser('~')
        jar = home + "/.stk/stacks/*/plugin-cdd-java/cdd.jar"

        for file in glob.glob(jar):
            return os.path.abspath(file)
            
    def clean_temp_files():
        if os.path.isdir('spooned'):
            import shutil
            shutil.rmtree('spooned')
    
    def download_cdd_file_if_needed():
        from os.path import exists
        if not exists("cdd.json"):
            import questionary
            download = questionary.select(
                "This project does not have the 'cdd.json' configuration file. Do you want to download a sample of it?",
                choices=["Yes", "No"],
            ).ask()

            if download == "Yes":
                import urllib.request
                try:
                    urllib.request.urlretrieve("https://raw.githubusercontent.com/gustavopintozup/plugin-cdd-java/main/cdd.json", "cdd.json")
                    print("Alright, 'cdd.json' file downloaded.")
                except:
                    print("We were unable to download the 'cdd.json' file. Please check your connection and try again.")
                    sys.exit(0)
            else:
                print("Without the 'cdd.json' file, we cannot perform the analysis.")
                sys.exit(0)

    download_cdd_file_if_needed()

    dir_cdd_jar = encontar_jar_cdd()
    target_project = str(metadata.target_path)

    comando_java = ["java", "-jar", dir_cdd_jar, "-p", target_project]

    print("Performing the source code analysis. It may take some time.")

    import subprocess
    result = subprocess.run(comando_java,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True)

    prettyprint(result)
        
    clean_temp_files()
            
    return metadata

def prettyprint(result):
    if result.returncode == 0:
        for item in result.stdout.split("\n"):
            print(item)
    else:
        for item in result.stderr.split("\n"):
            print(item)