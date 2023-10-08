# reduce() =        apply a function to an iterable and reduce it to a single cumulative value.
#                   Performs function on first two elements and repeats proces until one value remains.
#
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y : x+y, letters)
print(word)

factorial = [5,4,3,2,1]
result = functools.reduce(lambda x,y : x*y, factorial)
print(result)
