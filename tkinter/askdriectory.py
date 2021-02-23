from tkinter import *
from tkinter import ttk
from tkinter import filedialog
gui = Tk()
gui.geometry("400x400")
gui.title("FC")


def getDirPath():
    dir_selected = filedialog.askdirectory()
    dir_txt.set(dir_selected)


def doStuff():
    folder = dir_txt.get()
    print("Doing stuff with folder", folder)


dir_txt = StringVar()
a = Label(gui, text="Enter name")
a.grid(row=0, column=0)
# E = Entry(gui, textvariable=dir_txt)
E = Entry(gui, textvar=dir_txt)
E.grid(row=0, column=1)
btnFind = Button(gui, text="Browse Folder", command=getDirPath)
# btnFind = ttk.Button(gui, text="Browse Folder", command=getDirPath)
btnFind.grid(row=0, column=2)

c = ttk.Button(gui, text="find", command=doStuff)
c.grid(row=4, column=0)

save_img_path = Button(window, text='Browse', command='browse')
gui.mainloop()
