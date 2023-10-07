# dictionary            = a changeable, unordered collection of unique key:value pairs. Fast because they use hashing
#                       to allow us to access a value quickly

capitals = {"USA":"Washington DC",
            "Sweden":"Stockholm",
            "China":"Beijing",
            "Russia":"Moscow"}
print(capitals["China"])
# print(capitals["Moscow"])             # KeyError: 'Moscow'. values can only be accessed through the keys, not the other way around.
print(capitals.get("Germany"))          # No error. Returned value is 'None' if key does not exist.
print(capitals.keys())
print(capitals.values())
print("---")

for key,value in capitals.items():
    print(key, value)
print("---")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
print(capitals)
capitals.pop("China")
print(capitals)
capitals.clear()
print(capitals)             # empty dictionary
