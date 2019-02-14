from tkinter import *


def convert():
  kg = int(entry_val.get())
  gram = kg * 1000
  pound = kg * 2.20462
  ounce = kg * 35.274
  t1.insert(END, gram)
  t2.insert(END, pound)
  t3.insert(END, ounce)

window = Tk()

button = Button(window, text="Convert", command=convert)
button.grid(row=0, column=2)

entry_val = StringVar()
entry = Entry(window, textvariable=entry_val)
entry.grid(row=0, column=1)

label = Label(window, text="Kg")
label.grid(row=0, column=0)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()
