name = "daniella"
number = "234"
print(len(name))    # blank spaces count in length
print(name.find("a"))   # returns first occurence of "a" if multiple
print(name.upper())
print(name.lower())
print(name.isdigit())
print(number.isdigit())     # checks if string is digit, returns boolean
print(number.isalpha())     # checks if string contains only letters. returns False if spaces are included
print(name.count("a"))      # counts occurences of "a" in string
print(name.replace("a","o"))
print(name*3)