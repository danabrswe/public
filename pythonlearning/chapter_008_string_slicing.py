# slicing =     create a substring by extracting elements from another string
#               indexing[] or slice()
#               [start:stop:step]

name = "Daniel Abrahamsson"
first_name = name[0:6]          # stop index is exlusive
print(first_name)
print(len(first_name))
print(name[:6])                 # no start index assumes 0 as start
last_name = name[7:]
print(last_name)
print(len(last_name))
print(name[7::2])               # start at 7, stop at end of string and skip every second character
print(name[::-1])               # reversing the string. minus sign indicates stepping backwards.
print("---")

website = "http://www.google.com"
website2 = "http://www.wikipedia.com"
slice = slice(11,-4)            # create a slice object
print(website[slice])           # using slice object to create substring of "website" string
print(website2[slice])
