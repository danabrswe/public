# zip(*iterables) =     aggregate elements from two or more iterables.
#                       creates a zip object with paired elements stored in tuples for each element within our zip object

usernames = ["Dude","Bro","Mister"]
passwords = ["p@ssword","abc123","guest1"]
login_date =["20220101","20230213","20231004"]

users = dict(zip(usernames, passwords))         # stores returned zip object as a dictionary instead
print(users)

for key,value in users.items():
    print(key + ": " + value)
print("---")

print(users_with_login := list(zip(usernames,passwords,login_date)))