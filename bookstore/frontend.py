"""A program that stores book information."""


from tkinter import *

window = Tk()

l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l1 = Label(window, text='Author')
l1.grid(row=0, column=2)

l1 = Label(window, text='Year')
l1.grid(row=1, column=0)

l1 = Label(window, text='ISBN')
l1.grid(row=1, column=2)

window.mainloop()
