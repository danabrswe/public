from tkinter import *

scale_length = 400
window_width = 200

def submit():
    print("The temperature is " + str(scale.get()) + " degrees C.")

window = Tk()
window.geometry(str(window_width) + "x" +str(scale_length + 50))

scale = Scale(window,
              from_=200,
              to=0,
              length=scale_length,
              orient=VERTICAL,
              tickinterval=20,
              showvalue=0,
              troughcolor="#5eefff",
              fg = "#ff0000",
              bg = "#c2c2c2"
)
scale.set((scale["from"]-scale["to"]) / 2)
scale.pack()

button = Button(window,
                text = "submit",
                command=submit,
                )
button.pack()

window.mainloop()