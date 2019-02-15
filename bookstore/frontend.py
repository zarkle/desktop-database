"""The frontend code for a program that stores book information."""


from tkinter import *
import backend


def view_command():
    """Show all books in listbox."""
    lb.delete(0, END)
    for row in backend.view():
        lb.insert(END, row)


def search_command():
    """Search for a book."""
    lb.delete(0, END)
    for row in backend.search(title.get(), author.get(), year.get(), isbn.get()):
        lb.insert(END, row)


def add_command():
    """Add a new book."""
    backend.insert(title.get(), author.get(), year.get(), isbn.get())
    lb.delete(0, END)
    lb.insert(END, (title.get(), author.get(), year.get(), isbn.get()))


def get_selection(event):
    """Get the book info for the current selected row."""
    global selection
    idx = lb.curselection()[0]
    selection = lb.get(idx)
    e1.delete(0, END)
    e1.insert(END, selection[1])
    e2.delete(0, END)
    e2.insert(END, selection[2])
    e3.delete(0, END)
    e3.insert(END, selection[3])
    e4.delete(0, END)
    e4.insert(END, selection[4])


def delete_command():
    """Delete a book command."""
    backend.delete(selection[0])
    view_command()


def update_command():
    """Update a book record."""
    backend.update(selection[0], title.get(), author.get(), year.get(), isbn.get())
    lb.delete(0, END)
    lb.insert(END, (title.get(), author.get(), year.get(), isbn.get()))

window = Tk()
window.wm_title('Bookstore')

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

lb = Listbox(window, height=6, width=35, fg='white', bg='blue')
lb.grid(row=2, column=0, rowspan=6, columnspan=2)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>',get_selection)

b1 = Button(window, text='View All', width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text='Search Books', width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text='Add Book', width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text='Update Book', width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text='Delete Book', width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text='Exit', width=12, command=window.destroy)
b6.grid(row=7, column=3)

view_command()
window.mainloop()
