# tuple         = collection which is ordered and unchangeable. used to group together related data.

student = ("Daniel",32,"male")
print(student)
print(student.count("male"))
print(student.index("Daniel"))          # returns index of first "Daniel"
print("---")

for i in student:
    print(i)
print("---")

if 32 in student:
    print("The number 32 exists in the given tuple.")