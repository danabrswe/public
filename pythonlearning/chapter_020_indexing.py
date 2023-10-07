# index operator []         = gives access to a sequence's element (str, list, tuples)

name = "daniel abrahamsson"

if name[0].islower():               # first letter is changed to upper if lower
    name = name.capitalize()

print(name)

first_name = name[0:6].upper()
print(first_name)

last_name = name[-11:].capitalize()
print(last_name)

last_character = name[-1]
print(last_character)