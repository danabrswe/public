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