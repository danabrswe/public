import os

path1 = "pythonlearning\\test6.txt"
path2 = "pythonlearning\\testfolder4"

# remove file
try:
    os.remove(path1)

except FileNotFoundError as e:
    print(e)

except PermissionError as e:
    print(e)

else:
    print("file was removed")

# remove folder
try:
    #os.remove(path2)            # access denied error. cannot be used to remove directory.
    os.rmdir(path2)
    #shutil.rmtree(path2)       # removes folder even if contains files. requires "shutil" module. use with great caution.

except FileNotFoundError as e:
    print(e)

except PermissionError as e:
    print(e)

else:
    print("folder was removed")

finally:
    print("program done")