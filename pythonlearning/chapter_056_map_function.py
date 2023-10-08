# map() =       applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data : (data[0], round(data[1] * 0.9433, 2))

store_eur = list(map(to_euros, store))

for i in store_eur:
    print(i)