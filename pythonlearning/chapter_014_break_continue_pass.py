# Loop control statements       = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as placeholder

""" # example 1
while True:
    name = input("Enter your name: ")
    if name != "":
        break """

""" # example 2
phone_number = "123-456-7890"

for i in phone_number:
   if i == "-":
        continue
   print(i, end="")             # end="" ends each print with empty string instead of new line """

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i, end=" ")