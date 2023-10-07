import random

x = random.randint(1,6)
print(x)

y = random.random()             # random float in interval [0,1)
print(y)

my_list = ["rock","paper","scissors"]
z = random.choice(my_list)
print(z)

cards = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
random.shuffle(cards)
print(cards)