# label     = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()
window.geometry("1000x600")

photo = PhotoImage(file="pythonlearning\\box.png")

label = Label(window,
              text="Hello, World!",
              font=("Arial",40,"bold"),
              fg="#00ff00",
              bg="black",
              relief=SUNKEN,
              bd=10,
              padx=20,      # padding
              pady=20,
              image=photo,
              compound=RIGHT        # adds image to the right of previous item, the "Hello, World!" text
            )
label.pack()
#label.place(x=0,y=0)           # can be used instead of pack() for placing the label







window.mainloop()