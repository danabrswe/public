# list comprenhension =     a way to create a new list with less syntax.
#                           can mimic certain lambda function and are easier to read.
#                           list = [expession for item in iterable if conditional]
#                           list = [expression if condition else value for item in iterable]

squares = []                        # create an empty list
for i in range(1,11):               # create a for loop
    squares.append(i*i)             # define what each loop iteration should do
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)
print("---")

# example without list comprehension
students = [100,80,50,30,10]
print(students)
passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

# example with list comprehension
print(passed_students := [i for i in students if i >= 60])

# example with if/else statement
print(passed_students := [i if i >= 60 else "F" for i in students])