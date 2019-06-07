import os
import atexit
import subprocess

# This method gets called if the function exits normally
def cleanup():
    os.remove("testing_directory/main.cpp")
    os.remove("testing_directory/main.exe")
    os.remove("testing_directory/w01.py")


def main():
    if subprocess.call(["g++", "testing_directory/main.cpp","-o", "testing_directory/main" ]) ==0:
        subprocess.call("testing_directory/main.exe")
    #if os.system('g++ testing_directory/main.cpp' + ' -o testing_directory/main' ) ==0:
        #os.system("echo Code compiled")
        #os.system("echo Running main")
        #os.system('testing_directory\main')
    #else:
        #os.system("echo Code failed to compile")
        #os.system("echo -------------------")


if __name__ == "__main__":
    main()
atexit.register(cleanup);

