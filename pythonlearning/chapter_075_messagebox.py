from tkinter import *
from tkinter import messagebox

def click():
    # ok only
    """ messagebox.showinfo(title="this is an info message box", message="you are a person")
    messagebox.showwarning(title="warning!", message="YOU HAVE A VIRUS!!!")
    messagebox.showerror(title="error", message="something is wrong") """
  
    # ask ok cancel
    """ if messagebox.askokcancel(title="question", message="do you want to proceed?"):
        print("you proceed")
    else:
        print("you cancel") """

    # ask retry cancel
    """ if messagebox.askretrycancel(title="question", message="do you want to try again?"):
        print("you try again")
    else:
        print("you cancel") """

    # ask yes no
    """ if messagebox.askyesno(title="question", message="do you like cake?"):
        print("you like cake")
    else:
        print("you don't like cake") """
    
    # askquestion (returns string with "yes" or "no" instead of True/False)
    """ answer = messagebox.askquestion(message="do you like pie?")
    if answer == "yes":
        print("you like pie")
    else:
        print("you don't like pie") """
    
    # ask yes no cancel
    answer = messagebox.askyesnocancel(message = "do you like to code?")
    if answer == True:
        print("you like to code")
    elif answer == False:
        print("you don't like to code")
    else:
        print("you cancel")
    

window = Tk()

button = Button(window, command=click, text="click me") 
button.pack()

window.mainloop()