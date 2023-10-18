# radio button =    similar to checkbox, but you can only select one from a group

from tkinter import *


food = ["pizza","hamburger","hotdog"]
window = Tk()

def order():
    print("You ordered a " + food[x.get()] + ".")

pizza_image = PhotoImage(file="pythonlearning\\pizza.png")
hamburger_image = PhotoImage(file="pythonlearning\\burger.png")
hotdog_image = PhotoImage(file="pythonlearning\\hotdog.png")
food_images = [pizza_image,hamburger_image,hotdog_image]

x = IntVar()

for i in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[i],     # adds text to radiobuttons
                              variable=x,       # groups radiobuttons together if they share the same variable
                              value=i,          # assigns each radiobutton a different value
                              padx=20,          # adds padding on x-axis
                              font=("arial",18,"bold"),
                              image=food_images[i],
                              compound=RIGHT,
                              indicatoron=0,    # eliminate circle indicators
                              width=375,
                              command=order
                              )         
                
    radiobutton.pack(anchor=W)
    
window.mainloop()