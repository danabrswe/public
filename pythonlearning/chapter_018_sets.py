# set = collection which is unordered and unindexed. no duplicate values allowed.

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup"}

for i in utensils:
    print(i)
print("---")

utensils.add("napkin")
print(utensils)

utensils.remove("fork")
print(utensils)

utensils.update(dishes)
print(utensils)

utensils.clear()
print(utensils)
print("---")

utensils = {"fork","spoon","knife","knife","knife"}         # re-assigning starting values. duplicate values are dropped.
dishes = {"bowl","plate","cup","knife"}
print(utensils)
print(dishes)

dinner_table = utensils.union(dishes)
print(dinner_table)
print("---")

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))