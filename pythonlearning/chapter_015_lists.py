# list          = used to store mutiple items in a single variable

# each item is called an element

food = ["pizza","hamburger","hotdog"]
print(food[0])          # first position is 0
print("---")

food[0] = "sushi"
print(food[0])
print("---")

print(food)
print("---")

for i in food:
    print(i)
print("---")

food.append("ice cream")
print(food)

food.remove("hotdog")
print(food)

food.pop()
print(food)

food.insert(1, "cake")
print(food)

food.sort()
print(food)

food.clear()
print(food)             # list is now empty