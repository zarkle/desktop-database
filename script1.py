from tkinter import *

window = Tk()

b1 = Button(window, text="Execute")
b1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=0, column=1)

window.mainloop()
