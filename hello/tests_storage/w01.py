import os
import subprocess
import atexit
import shutil


# This method gets called if the function exits normally
def cleanup():
    print('This is where and when file cleanup happens')
    selfDestrcut()


# This code destroys itself after the code executes
def selfDestrcut():
    if os.path.exists("testing_directory/w01.py"):
        os.remove("testing_directory/w01.py")
        os.remove("testing_directory/main.exe")
        os.remove("testing_directory/main.cpp")
    else:
        print("The file does not exist")


def main():
    os.system("echo Compiling main")
    os.system("echo -------------------")
    shutil.copy('main.cpp', 'testing_directory/')
    if os.system('g++ testing_directory/main.cpp' + ' -o testing_directory/main' ) ==0:
        os.system("echo Code compiled")
        os.system("echo -------------------")
        os.system("echo Running main")
        os.system("echo -------------------")
        os.system('testing_directory\main')
    else:
        os.system("echo Code failed to compile")
        os.system("echo -------------------")

if __name__ == "__main__":
    main()
atexit.register(cleanup);

