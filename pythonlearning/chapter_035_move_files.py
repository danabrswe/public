import os

source_file = "pythonlearning\\test5.txt"
destination_file = "pythonlearning\\testfolder2\\test5.txt"

source_folder = "pythonlearning\\testfolder3"
destination_folder = "pythonlearning\\testfolder2\\testfolder3"

try:
    if os.path.exists(destination_file):
        print("destination already has a file. file will not be moved to destination. move the destination file back to source.")
    else:
        os.replace(source_file,destination_file)
        print(source_file + " was moved")

except FileNotFoundError as e:
    print(e)

# can be used to move folders too
try:
    if os.path.exists(destination_folder):
        print("destination already has a folder. folder will not be moved to destination. move the destination folder back to source.")
    else:
        os.replace(source_folder,destination_folder)
        print(source_folder + " was moved")

except FileExistsError as e:
    print(e)
