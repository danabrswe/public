try:
    with open("pythonlearning\\test2.txt") as file:
        print(file.read())
    print(file.closed)          # check if file is closed. important to close files to save resources.

except FileNotFoundError as e:
    print (e)