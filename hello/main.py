import atexit
import os
import argparse
import shutil
from pathlib import Path


def selfdestruct():
    if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
    else:
        print("The file does not exist")


def testconfig():
    print("\n\nTESTING USER CONFIGURATION")
    directorycheck()


def directorycheck():
    print("\nTEST 1: Checking for directory...")
    my_file = Path("testDirectory/")
    if my_file.is_dir():
        print("Status:\t\tSUCCESS")
        filecheck()
    else:
        print('Status:\t\tFAIL')


def filecheck():
    print("\nTEST 2: Checking for empty directory")
    my_file = Path("testDirectory/demo.py")
    if my_file.exists():
        print("Status: FAILURE\nRetrying...")
        os.remove("testDirectory/demo.py")
        filecheck()
    else:
        print("Status:\t\tSUCCESS")
        copycheck()


def copycheck():
    print("\nTEST 3: Pulling file test")
    shutil.copy('demo.py', 'testDirectory/')
    my_file = Path("testDirectory/demo.py")
    if my_file.exists():
        print("Status:\t\tSUCCESS")
        deletecheck()
    else:
        print("Status:\t\tFAILURE")


def deletecheck():
    print("\nTEST 4: Deleting file check")
    os.remove("testDirectory/demo.py")
    my_file = Path("testDirectory/demo.py")
    if my_file.exists():
        print("Status:\t\tFAILURE")
    else:
        print("Status:\t\tSUCCESS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--test", help="Checks users config",
                        action="store_true")
    args = parser.parse_args()

    shutil.copy('venv/w01.py', 'testDirectory/')
    os.system('python testDirectory/w01.py')
    if args.test:
        testconfig()


if __name__ == "__main__":
    main()


