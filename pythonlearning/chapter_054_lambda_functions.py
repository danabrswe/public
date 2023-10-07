# lambda function =     function written in one line using lambda keyword.
#                       accepts any number of arguments but only as one expression.

#                       thnk of it as a shortcut.
#                       useful if needed for a short period of time, then throw-away

# lambda_parameters:expression

# example without lambda expression
def double(x):
    return x*2
print(double(5))

# example with lambda expression
double = lambda x : x*2
print(double(10))

# another example
multiply = lambda x, y : x * y
print(multiply(3,10))

# another example
age_check = lambda age : True if age >= 18 else False
print(age_check(20))