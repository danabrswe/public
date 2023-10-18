# also called checkbutton

from tkinter import *

def display():
    if(x.get() == True):
        print("You agree")
    else:
        print("You don't agree")

window = Tk()

x = BooleanVar()

box = PhotoImage(file="pythonlearning\\box.png")

check_button = Checkbutton(window,
                           text = "I agree",
                           variable = x,
                           onvalue = True,
                           offvalue = False,
                           command=display,
                           font=("arial",16,"bold"),
                           fg="#00ff00",
                           bg="black",
                           activeforeground="#00ff00",
                           activebackground="black",
                           image=box,
                           compound="right")
check_button.pack()

window.mainloop()