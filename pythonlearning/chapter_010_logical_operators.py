# logical operators (and, or, not)      = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today.\nGo outside.")        # the \n escape sequence inserts new line
elif temp < 0 or temp > 30:
    print("The temperature is bad today.\nStay inside.")
print("---")

print(not(True))