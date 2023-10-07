# function          = a block of code which is executed only when it is called. aka "invoking a function".

def hello(first_name, last_name):                # defining the function
    print("Hello " +first_name + " " + last_name + "!")
    print("Have a nice day.")
    print("---")

my_first_name = "Daniel"
my_last_name = "Abrahamsson"

hello(my_first_name, my_last_name)                     # calling the function "hello"

for i in range(3):          # calls the function three times with "Ben" as name
    hello("Ben","Armstrong")