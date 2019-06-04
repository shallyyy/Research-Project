import atexit
import os


# This method gets called if the function exits normally
def cleanup():
    print('This is where and when file cleanup happens')
    selfDestrcut()


# This code destroys itself after the code executes
def selfDestrcut():
    if os.path.exists("selfDestruct.py"):
        os.remove("selfDestruct.py")
    else:
        print("The file does not exist")


def main():
    print("Main executed");


if __name__ == "__main__":
    main()

# This handles the termination fo the program
atexit.register(cleanup);
