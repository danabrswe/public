# higher order functions        = a function that either:
#                               1. accepts a function as an argument
#                               2. returns a function
#
#                               in python functions are also treated as objects

# example 1: function that accepts a function as argument

def loud(text):
    return "(shouting) " + text.upper()

def quiet(text):
    return "(whispering) " + text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
print("---")

# example 2: fucntion that returns a function
def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)         # sets x = 2 in y/x
print(divide(20))           # sets y = 20 in y/x and returns y/x as float --> 20/2 = 10.0