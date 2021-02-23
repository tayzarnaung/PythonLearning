from tkinter import *
from tkinter import messagebox
import tkinter.messagebox


# ****** GLOBAL VARIABLES ******

objects = []
window = Tk()
window.withdraw()
window.title('Email Storage')


class popupWindow:

    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.title('Input Password')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", font=(
            'Courier', 14), justify=CENTER)
        self.l.pack()
        self.e = Entry(top, show='*', width=30)
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit',
                        command=self.cleanup, font=('Courier', 14))
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        access = ' '

        if self.value == access:
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e.delete(0, 'end')
            messagebox.showerror(
                'Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))


class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        f = open('emails.txt', "a")

        encryptedN = encryptedE = encryptedP = ""

        for letter in self.name:
            if letter == ' ':
                encryptedN += ' '
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in self.email:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in self.password:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class entity_display:

    def __init__(self, master, n, e, p, row_count):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.row_count = row_count

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.lbl_name = Label(
            self.window, text=dencryptedN, font=('Courier', 14))
        self.lbl_email = Label(
            self.window, text=dencryptedE, font=('Courier', 14))
        self.lbl_pass = Label(
            self.window, text=dencryptedP, font=('Courier', 14))
        self.deleteBtn = Button(self.window, text='X',
                                fg='red', command=self.delete)

    def display(self):
        self.lbl_name.grid(row=6 + self.row_count, sticky=W)
        self.lbl_email.grid(row=6 + self.row_count, column=1)
        self.lbl_pass.grid(row=6 + self.row_count, column=2, sticky=E)
        self.deleteBtn.grid(row=6 + self.row_count, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion(
            'Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for obj in objects:
                print(obj)
                obj.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.row_count:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.lbl_name.destroy()
        self.lbl_email.destroy()
        self.lbl_pass.destroy()
        self.deleteBtn.destroy()


# ******* FUNCTIONS *********


def onsubmit():
    n = name.get()
    p = password.get()
    e = email.get()

    entity = entity_add(window, n, p, e)
    entity.write()

    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')

    messagebox.showinfo('Added Entity', 'Successfully Added, \n' +
                        'Name: ' + n + '\nEmail: ' + e + '\nPassword: ' + p)
    readfile()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(
            window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()


# ******* GRAPHICS *********

popupWindow(window)

entity_lbl = Label(window, text='Add Entity', font=('Courier', 18))
name_lbl = Label(window, text='Name: ')
email_lbl = Label(window, text='Email: ')
pass_lbl = Label(window, text='Password: ')
name = Entry(window, font=('Courier', 14))
email = Entry(window, font=('Courier', 14))
password = Entry(window, show='*', font=('Courier', 14))
submit = Button(window, text='Add Email',
                command=onsubmit, font=('Courier', 14))

entity_lbl.grid(columnspan=3)
name_lbl.grid(row=1, sticky=E, padx=3)
email_lbl.grid(row=2, sticky=E, padx=3)
pass_lbl.grid(row=3, sticky=E, padx=3)

name.grid(row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_lbl2 = Label(window, text='Name: ', font=('Courier', 14))
email_lbl2 = Label(window, text='Email: ', font=('Courier', 14))
pass_lbl2 = Label(window, text='Password: ', font=('Courier', 14))

name_lbl2.grid(row=5)
email_lbl2.grid(row=5, column=1)
pass_lbl2.grid(row=5, column=2)

readfile()

window.mainloop()
