# for loop          = a statement that will execute its code block a limited amount of times

#                   while loop could be unlimited but for loops are limited if used correctly

import time

for i in range(10):
    print(i+1)
print("---")

for i in range(50,100+1,2):
    print(i)
print("---")

for i in "Daniel Abrahamsson":
    print(i)
print("---")

for seconds in range(5,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year!")