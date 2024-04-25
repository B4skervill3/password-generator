from tkinter import *
import random
import string

# Generator source code


def generator():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    password_length = int(length_Box.get())

    passwordField.delete(0, END)

# To determine the user's desired criteria
    if choice1.get():
        passwordField.insert(0, random.sample(small_letters+capital_letters, password_length))
        if choice2.get():
            passwordField.delete(0, END)
            passwordField.insert(0, random.sample(small_letters+capital_letters+symbols, password_length))
            if choice3.get():
                passwordField.delete(0, END)
                passwordField.insert(0, random.sample(small_letters+capital_letters+numbers+symbols, password_length))
        elif choice3.get():
            passwordField.delete(0, END)
            passwordField.insert(0, random.sample(small_letters+capital_letters+numbers, password_length))

    elif choice2.get():
        passwordField.insert(0, random.sample(small_letters+symbols, password_length))
        if choice3.get():
            passwordField.delete(0, END)
            passwordField.insert(0, random.sample(small_letters+symbols+numbers, password_length))

    elif choice3.get():
        passwordField.delete(0, END)
        passwordField.insert(0, random.sample(small_letters+numbers, password_length))

    else:
        passwordField.delete(0, END)
        passwordField.insert(0, random.sample(small_letters, password_length))


def copier():
    root.clipboard_clear()
    root.clipboard_append(passwordField.get())


# Main display window


root = Tk()
root.title('Password Generator')
root.config(bg='gray15')
password_label = Label(root, text='Password Generator', font=('jetbrains mono', 20, 'bold'), bg='gray15', fg='white')
password_label.grid()
bFont = ('jetbrains mono', 15, 'bold')

# Buttons and other interactions

# Password Length
pLength_label = Label(root, text='Password Length', font=('jetbrains mono', 15, 'bold'), bg='gray15', fg='white')
pLength_label.grid()
length_Box = Spinbox(root, from_=6, to_=18, width=5, font=bFont)
length_Box.grid(pady=7)

# Password Criteria
choice1 = IntVar()
choice2 = IntVar()
choice3 = IntVar()
sFont = ('jetbrains mono', 10, 'bold')

uplowcheckButton = Checkbutton(root, text='Include uppercase', variable=choice1, font=sFont)
uplowcheckButton.grid(pady=3)

symcheckButton = Checkbutton(root, text='Include symbols', variable=choice2, font=sFont)
symcheckButton.grid(pady=3)

numcheckButton = Checkbutton(root, text='Include numbers', variable=choice3, font=sFont)
numcheckButton.grid(pady=3)

# Generated Password
generateButton = Button(root, text='Generate', font=bFont, command=generator)
generateButton.grid(pady=7)

passwordField = Entry(root, width=35, bd=2, font=sFont)
passwordField.grid()

copyButton = Button(root, text='Copy', font=sFont, command=copier)
copyButton.grid(pady=7)

root.mainloop()
