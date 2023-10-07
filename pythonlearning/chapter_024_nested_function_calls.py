# nested functions calls        = functions calls inside other functions calls.
#                               innermost function calls are resolved first.
#                               returned value is used as argument for the next outer function

# example that could be written with only one line
""" num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num) """

print(round(abs(float(input("Enter a whole positive number: ")))))