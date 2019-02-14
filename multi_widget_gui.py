from tkinter import *
from tkinter.ttk import *

window = Tk()

button = Button(window, text="Convert")
button.grid(row=0, column=2)

entry_val = StringVar()
entry = Entry(window, textvariable=entry_val)
entry.grid(row=0, column=1)

label = Label(window, text="Kg")
label.grid(row=0, column=0)

window.mainloop()
