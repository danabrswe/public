text = "This text has been written by your program.\nThe second line of the text starts here.\nHere's the third and last line."

with open("pythonlearning\\test3.txt","w") as file:             # "w" overwrites existing files
    file.write(text)

with open("pythonlearning\\test3.txt","a") as file:             # "a" to append a file instead of overwriting
    file.write("\nHere is another line of text!")
