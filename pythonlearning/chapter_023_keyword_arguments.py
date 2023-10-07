# keyword arguments =   arguments proceded by an identifier when we pass them to a function.
#                       The order of the arguments doesn't matter, unlike positional arguments.
#                       Python knows the names of the arguments that our function receives.

def hello(first, middle, last):
    print("Hello " + first.capitalize() + " " + middle.capitalize() + " " + last.capitalize() + "!")

hello(last="abrahamsson", first="daniel", middle="unknown")