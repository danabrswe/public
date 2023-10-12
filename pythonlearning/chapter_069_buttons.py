# buttons       = you blick it, then it does stuff

from tkinter import *

count = 0

def click():
    global count
    count += 1
    print("You've now clicked the button",count,"times.")

window = Tk()

photo = PhotoImage(file="pythonlearning\\box.png")

button = Button(window,
                text="Click me!",
                command=click,          # this is called a callback
                font=("Comic Sans",30),
                fg="#00ff00",
                bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                #state=DISABLED,         # can no longer be used, becomes gray/unavailable
                image=photo,
                compound=TOP
                )

button.pack()

window.mainloop()