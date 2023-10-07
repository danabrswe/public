# str.format() =        optional method that gives users.
#                       gives more control when displaying output

animal = "cow"
item = "moon"

# bad example
#print("The " + animal + " jumped over the " + item)

# better example
print("The {} jumped over the {}".format(animal,item))

print("The {1} jumped over the {0}".format(animal,item))            # positional arguments
print("{person2} jumped over {person1}".format(person1="Bro",person2="Daniel"))
print("The {0} jumped over the {0} that jumped over the {0}".format(animal))
print("The {animal} jumped over the {animal} that jumped over the {animal}".format(animal="monkey"))
print("---")

# even better example
text = "The {} jumped over the {}"
print(text.format("cow","moon"))
print("---")

# example: add padding
name = "Daniel"
print("Hello, my name is {}".format(name))
print("Hello, my name is {name:10}. Nice to meet you.".format(name="Daniel"))
print("Hello, my name is {name:<10}. Nice to meet you.".format(name="Daniel"))   # left alignment is default
print("Hello, my name is {name:>10}. Nice to meet you.".format(name="Daniel"))
print("Hello, my name is {name:^10}. Nice to meet you.".format(name="Daniel"))
print("---")

pi = 3.14159
number1 = 1000000
number2 = 1000
print("The number pi is {:.3f}".format(pi))         # displaying as float with 3 decimal places.
                                                    # this rounds the float before displaying the digits
print("The number pi is {:,}".format(number1))      # with thousands separator
print("The number pi is {:o}".format(number2))      # as octal number
print("The number pi is {:X}".format(number2))      # as hexadec
print("The number pi is {:e}".format(number2))      # scientific notation with lower case "e"""
print("The number pi is {:E}".format(number2))      # scientific with upper case