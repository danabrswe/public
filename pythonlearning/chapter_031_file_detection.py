import os

text_file = "pythonlearning\\test1.txt"
folder = "pythonlearning\\testfolder1"

if os.path.exists(text_file):
    print("location exists")
    if os.path.isfile(text_file):
        print("location is a file")
    elif os.path.isdir(text_file):
        print("location is a directory")
else:
    print("location does not exist")
print("---")

if os.path.exists(folder):
    print("location exists")
    if os.path.isfile(folder):
        print("location is a file")
    elif os.path.isdir(folder):
        print("location is a directory")
else:
    print("location does not exist")