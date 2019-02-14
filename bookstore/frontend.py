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

lb = Listbox(window, height=6, width=3)
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

b1 = Button(window, text='View All', width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Books', width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Book', width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Book', width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Book', width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text='Exit', width=12)
b6.grid(row=7, column=3)

window.mainloop()
