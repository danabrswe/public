from tkinter import *

window = Tk()       # instantiate an instance of a window
window.geometry("800x600")
window.title("GUI main window")

icon = PhotoImage(file="pythonlearning\\box.png")       # create PhotoImage object from png file
window.iconphoto(True,icon)     # set icon for window using PhotoImage
window.config(background="#ebc934")     # set background color

window.mainloop()       # place window on screen. listen for events.