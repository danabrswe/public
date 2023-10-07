# while loop =      a statement that will execute its code block as long as its condition remains true

""" # infinite loop example
while True:
    print("Help! I'm stuck in an infinite loop!") """

""" # example of while loop that breaks when name string is not empty
name = ""            # using None object doesn't work with len() as None objects have no length

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name.capitalize() + "!") """

# example using boolean
name = None             # None objects evaluate to False
while not name:
    name = input("Input your name: ")           # empty strings evaluate to False, non-empty strings to True
print("Hello " + name.capitalize() + "!")