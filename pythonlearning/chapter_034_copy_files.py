# copyfile()        = copies contents of a file
# copy()            = copyfile() + permission mode + destination can be directory
# copy2()           = copy() + copies metadata, a file's creation and modification times

import shutil

shutil.copy2("pythonlearning\\test4.txt","pythonlearning\\test4_copy.txt")               # args: src, dest