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

title = StringVar()
e1 = Entry(window, textvariable=title)
e1.grid(row=0, column=1)

author = StringVar()
e2 = Entry(window, textvariable=author)
e2.grid(row=0, column=3)

year = StringVar()
e3 = Entry(window, textvariable=year)
e3.grid(row=1, column=1)

isbn = StringVar()
e4 = Entry(window, textvariable=isbn)
e4.grid(row=1, column=3)

window.mainloop()
