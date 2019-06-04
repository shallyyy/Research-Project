import atexit


# This method gets called if the function exits normally
def cleanup():
    print('This is where and when file cleanup happens')


def main():
    print("Main executed");


if __name__ == "__main__":
    main()

# This handles the termination fo the program
atexit.register(cleanup);
