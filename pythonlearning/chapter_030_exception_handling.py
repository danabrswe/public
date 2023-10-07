# exception         = events detected during exection that interrups the normal flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print("error: " + str(e))
except ValueError as e:
    print("error: " + str(e))
except Exception as e:
    print("error: " + str(e))

else:
    print(result)

finally:
    print("program done")