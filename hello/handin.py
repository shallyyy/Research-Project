import atexit
import os
import argparse
import shutil
from pathlib import Path


def filecleanup():
    if os.path.exists("w01.py"):
        os.remove("w01.py")


def directorycheck():
    if Path("testing_directory/").is_dir():
        print("TEST 1: Checking for directory\nStatus:\t\tSUCCESS\n")
        filecheck()
    else:
        print('TEST 1: Checking for directory\nStatus:\t\tFAIL\n')


def filecheck():
    os.remove("testing_directory/w01.py")
    if Path("testing_directory/w01.py").exists():
        print("TEST 2: Checking for empty directory\nStatus: FAILURE\nRetrying...\n")
    else:
        print("TEST 2: Checking for empty directory\nStatus:\t\tSUCCESS\n")
        copycheck()


def copycheck():
    shutil.copy('tests_storage/w01.py', 'testing_directory/')
    if Path("testing_directory/w01.py").exists():
        print("TEST 3: Pulling file test\nStatus:\t\tSUCCESS\n")
        deletecheck()
    else:
        print("TEST 3: Pulling file test\nStatus:\t\tFAILURE\n")


def deletecheck():
    os.remove("testing_directory/w01.py")
    if Path("testing_directory/w01.py").exists():
        print("TEST 4: Deleting file check\nStatus:\t\tFAILURE\n")
    else:
        print("TEST 4: Deleting file check\nStatus:\t\tSUCCESS\n")


def send_register_email(ulid):
    os.system("python email_storage/emailTest.py " + str(ulid) + " -r ")


def run_submission():
    shutil.copy('tests_storage/w01.py', 'testing_directory/')
    os.system('python testing_directory/w01.py')


def token_check():
    if Path("token.txt").exists():
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id",               help="ul id",               type=int)
    parser.add_argument("-t", "--test",     help="Checks users config", action="store_true")
    parser.add_argument("-r", "--register", help="Checks users config", action="store_true")
    parser.add_argument("-s", "--submit",   help="Submission handin",   action="store_true")
    args = parser.parse_args()

    if args.test:
        directorycheck()
    elif args.register:
        send_register_email(args.id)
    elif args.handin:
        run_submission()


if __name__ == "__main__":
    main()


