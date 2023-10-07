# **kwargs =        parameter that will pack all arguments into a dictionary.
#                   useful so that a function can accept a varying amount of keyword arguments.

def hello(first, last):
        print("Hello " + first + " " + last)

#hello(first="Daniel", middle="Unknown", last="Abrahamsson")        # error becuase wrong amount of keyword arguments.

def hello(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["last"])
    print("---")

hello(first="Daniel", middle="Unknown", last="Abrahamsson")

def hello(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
    print("\n---")

hello(name1="Daniel",name2="Abra",name3="Kadabra",name4="Abrahamsson")