from string import Template


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    newfilename = input("Enter the name of your test file:\n")  # Python 3
    file = open(newfilename + ".py", "w+")
    testfilename = input("Enter the name of the file students will be testing:\n")
    filename = testfilename

    message_template = read_template("template.txt")
    message = message_template.substitute(CPPFILE=filename, PYFILE=newfilename)
    file.write(message)


    #testCases = input("Enter the amount of test cases:\n")
    # for i in text:
    #    pass
    #   inputTest = input("Enter the first input\n")
    #    outputTest = input("Enter the expected output of that test\n")
    #   file.write(inputTest + outputTest)


if __name__ == '__main__':
    main()