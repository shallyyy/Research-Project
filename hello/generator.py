import sys
text = input("Enter the name of your test file:\n")  # Python 3
file = open(text+".py", "w+")
text = input("Enter the name of the file students will be testing:\n")
filename = text
text = input("Enter the amount of test cases:\n")
for i in text:
    inputTest = input("Enter the first input\n")
    outputTest = input("Enter the expected output of that test\n")
    file.write(inputTest+outputTest)
