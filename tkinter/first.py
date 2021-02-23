from tkinter import *


window = Tk()
window.title("Tkinter Test")
window.configure(background='black')


def click():
    print(textentry.get())
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        text = my_dict[entered_text]
    except KeyError:
        text = "Sorry there is no word like that."
    output.insert(END, text)


def close_window():
    window.destroy()
    exit()
    
# Open window having dimension 100x100
# window.geometry('100x100')

# btn = Button(window, text='Quit !', bd='5', command=window.destroy)
# btn.pack(side='top')

# canvas = Canvas(window, width=600, height=300)
# canvas.grid(columnspan=3)

photo1 = PhotoImage(file='lena.png')
Label(window, image=photo1, bg='black').grid(row=0, column=0, sticky=E)

Label(window, text='Enter the word you like to find in dict: ', bg='black',
      fg='white', font='none 12 bold').grid(row=1, column=0, sticky=W)

textentry = Entry(window, width=20, bg='white')
textentry.grid(row=1, column=0, sticky=E)

Button(window, text="Search", width=6, command=click).grid(
    row=3, column=0, sticky=W)
Button(window, text="Quit", width=6, command=close_window).grid(
    row=3, column=0, sticky=E)

Label(window, text='\ntext:', bg='black', fg='white',
      font='none 12 bold').grid(row=4, column=0, sticky=W)

output = Text(window, width=75, height=6, wrap=WORD, background='white')
output.grid(row=5, column=0, columnspan=2, sticky=W)

my_dict = {
    'algorithm': 'Step by step instructions', 'bug': 'piece of code'
}

window.mainloop()
