# *args          = parameter that will pack all arguments into a tuple.
#               useful so that a function can accept a varying amount of arguments.
#               common convention to name it "args".

def add(*args):
    sum = 0
    args = list(args)           # items in tuples cannot be changed. could for instance be casted into a list first.
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))