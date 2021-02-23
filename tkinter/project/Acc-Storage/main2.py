from tkinter import *
from tkinter import messagebox
import tkinter.messagebox


class popupWindow:

    attempts = 0

    def __init__(self):
        top = self.top = Toplevel()
        top.title('Input Password')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", justify=CENTER)
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


class AccountEntity:

    def __init__(self, n, e, p, row_count=None):
        self.name = n
        self.email = e
        self.password = p
        self.row_count = row_count

    def write(self):
        f = open('emails.txt', "a")

        def encrypt(words):
            encrypt = ''
            for letter in words:
                if letter == ' ':
                    encrypt += ' '
                else:
                    encrypt += chr(ord(letter) + 5)

            return encrypt

        f.write(encrypt(self.name) + ',' + encrypt(self.email) + ',' + encrypt(self.password) + ', \n')
        f.close()

    def decryptTexts(self):
        def decrypt(words):
            decrypt = ''
            for letter in words:
                if letter == ' ':
                    decrypt += ' '
                else:
                    decrypt += chr(ord(letter) - 5)
            return decrypt
            
        self.dencryptedN = decrypt(self.name)
        self.dencryptedE = decrypt(self.email)
        self.dencryptedP = decrypt(self.password)
      

    def display(self):
        self.decryptTexts()

        self.lbl_name = Label(
            window, text=self.dencryptedN, font=('Courier', 14))
        self.lbl_email = Label(
            window, text=self.dencryptedE, font=('Courier', 14))
        self.lbl_pass = Label(
            window, text=self.dencryptedP, font=('Courier', 14))
        self.deleteBtn = Button(
            window, text='X', fg='red', command=self.delete)

        self.lbl_name.grid(row=6 + self.row_count, sticky=W)
        self.lbl_email.grid(row=6 + self.row_count, column=1)
        self.lbl_pass.grid(row=6 + self.row_count, column=2, sticky=E)
        self.deleteBtn.grid(row=6 + self.row_count, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion(
            'Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for obj in accountEntiy_objs:
                obj.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            row_count = 0

            for line in lines:
                if row_count != self.row_count:
                    f.write(line)
                    row_count += 1

            f.close()
            readfile()

    def destroy(self):
        self.lbl_name.destroy()
        self.lbl_email.destroy()
        self.lbl_pass.destroy()
        self.deleteBtn.destroy()


# ******* FUNCTIONS *********


def onSubmit():
    n = name.get()
    e = email.get()
    p = password.get()

    entity = AccountEntity(n, e, p)
    entity.write()

    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')

    messagebox.showinfo('Added Entity', 'Successfully Added, \n' +
                        'Name: ' + n + '\nEmail: ' + e + '\nPassword: ' + p)
    readfile()


def readfile():
    f = open('emails.txt', 'r')
    row_count = 0

    for line in f:
        entityList = line.split(',')
        e = AccountEntity(
            entityList[0], entityList[1], entityList[2], row_count)

        accountEntiy_objs.append(e)
        e.display()
        row_count += 1
    f.close()


# ****** GLOBAL VARIABLES ******
accountEntiy_objs = []
window = Tk()
window.title('Email Storage')
window.withdraw()

# ******* GRAPHICS *********
popupWindow()

entity_lbl = Label(window, text='Add Entity', font=('Courier', 18))
name_lbl = Label(window, text='Name: ')
email_lbl = Label(window, text='Email: ')
pass_lbl = Label(window, text='Password: ')
name = Entry(window, font=('Courier', 14))
email = Entry(window, font=('Courier', 14))
password = Entry(window, show='*', font=('Courier', 14))
submit = Button(window, text='Add Email',
                command=onSubmit, font=('Courier', 14))

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
