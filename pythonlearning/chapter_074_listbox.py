# listbox = a listing of selectable text items within its own container

from tkinter import *

def add():
    if entry_box.get() != "":
        listbox.insert(listbox.size(), entry_box.get())
        listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    
    listbox.config(height=listbox.size())

def submit():
    if listbox.curselection() != ():
        print("You have ordered: ")

        for i in listbox.curselection():
            print(listbox.get(i))

        print("---")

# main body of program starts here
if __name__ == "__main__":
    
    window = Tk()

    listbox = Listbox(window,
                    bg="#fcdf74",
                    font=("times new roman",35,"bold"),
                    selectmode=MULTIPLE)
    listbox.pack()

    listbox.insert(0,"pizza")
    listbox.insert(1,"pasta")
    listbox.insert(2,"garlic bread")
    listbox.insert(3,"soup")
    listbox.insert(4,"salad")

    listbox.config(width=15)
    listbox.config(height=listbox.size())       # height adjusts dynamically with the number of list items

    entry_box = Entry(window)
    entry_box.pack()

    add_button = Button(window, text="add", command=add)
    add_button.pack()

    submit_button = Button(window, text="submit", command=submit)
    submit_button.pack()

    delete_button = Button(window, text="delete", command=delete)
    delete_button.pack()

    window.mainloop()