import tkinter
from tkinter import *


def callback(input):

    if input.isdigit():
        print(input)
        return True

    elif input == "":
        print(input)
        return True

    else:
        print(input)
        return False


parent = Tk()
parent.geometry('640x480')

e = Entry(parent, bg='gray')
e.place(x=10, y=200)
reg = parent.register(callback)

e.config(validate="key", validatecommand=(reg, '%P'))


def only_numbers(char):
    return char.isdigit()


validation = parent.register(only_numbers)
# entry = Entry(parent, bg='gray', validate="key", validatecommand=(validation, '%S'))
entry = Entry(parent, bg='gray')
entry.config(validate="key", validatecommand=(validation, '%S'))
entry.pack()


parent.mainloop()
