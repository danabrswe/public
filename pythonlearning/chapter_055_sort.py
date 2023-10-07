# sort() method             = used with lists
# sort() function           = used with iterables

students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]
cars = ("Volvo","Tesla","Porsche","BMW","Audi")

# sort list using sort method
students.sort(reverse=True)     # reverse keyword to do reversed sort order

for i in students:
    print(i)
print("---")

# sort tuple using sort function
#cars.sort()            # AttributeError. does not work with tuples
sorted_cars = sorted(cars, reverse=True)       # returns list but accepts other iterables
print(type(sorted_cars))
print(sorted_cars)

for i in sorted_cars:
    print(i)
print("---")

students = [("Daniel","A",92),
            ("Alice","C",72),
            ("Bob","E",51),
            ("Spongebob","B",80),
            ("Gary","A",99)]

students.sort()         # sort by name (first "column")
print(students)

for i in students:
    print(i)
print("---")

score = lambda students : students[2]       # lambda function to get element with index 2 in tuples in "students"
students.sort(key=score, reverse=True)
print(students)

for i in students:
    print(i)