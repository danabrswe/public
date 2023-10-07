def hello():
    print("Hello")

print(type(hello))      # prints the type of the object assigned to the variable "hello"
print(hello)            # prints the type of the object assigned and the address of where it's stored in memory

hi = hello              # new reference variable that refers to the same object, function "hello", stored in the same place in memory
print(hi)

hi()                    # the new reference variable "hi" can be used to call the function "hello"

# example 2
say = print
say("TEST MESSAGE")