import atexit
import os
import argparse
import shutil
from pathlib import Path


def selfdestruct():
    if os.path.exists("w01.txt"):
        os.remove("w01.txt")
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
    shutil.copy('venv/w01.py', 'testDirectory/')
    my_file = Path("testDirectory/w01.py")
    if my_file.exists():
        print("Status:\t\tSUCCESS")
        deletecheck()
    else:
        print("Status:\t\tFAILURE")


def deletecheck():
    print("\nTEST 4: Deleting file check")
    os.remove("testDirectory/w01.py")
    my_file = Path("testDirectory/w01.py")
    if my_file.exists():
        print("Status:\t\tFAILURE")
    else:
        print("Status:\t\tSUCCESS")


def send_register_email(ulid):
    os.system("python email/email.py " + str(ulid) + "-r ")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="ul id",
                        type=int)
    parser.add_argument("-t","--test", help="Checks users config",
                        action="store_true")
    parser.add_argument("-r", "--register", help="Checks users config",
                        action="store_true")
    args = parser.parse_args()

    shutil.copy('venv/w01.py', 'testDirectory/')
    os.system('python testDirectory/w01.py')
    ulid = args.id
    if args.test:
        testconfig()
    if args.register:
        send_register_email(ulid)
        

if __name__ == "__main__":
    main()


