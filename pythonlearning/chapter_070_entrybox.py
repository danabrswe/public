# entrybox / entry widget       = textbox that accepts a single line of user input

from tkinter import *

def submit():
    password = entry.get()
    print("Your password is " + '"' + password + '".')
    entry.config(state=DISABLED)

# clears entrybox from input
def clear():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial",30,"bold"),
              fg="#00ff00",
              bg="black",
              show="*")      # show other character than input
entry.insert(0,"default_password")
entry.pack()

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="clear",command=clear)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()