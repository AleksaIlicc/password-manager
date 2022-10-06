from tkinter import *
from tkinter import messagebox
import random

my_email = "aleks.ilic05@gmail.com" #base mail
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#pass_generator

def generate_pass():
    pass_let = [random.choice(letters) for _ in range(8)]
    pass_sym = [random.choice(symbols) for _ in range(2)]
    pass_num = [random.choice(numbers) for _ in range(1)]

    password_list = pass_let+pass_num+pass_sym
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

#saving_pass_data

def add_click():

    site = website_entry.get()
    pw = password_entry.get()
    mail = username_entry.get()
    if len(site) == 0 or len(pw) == 0 or len(mail) == 0:
        messagebox.showinfo(
            title="Oops", message="Some of your fields are empty, please fill all your fields.")
    else:
        is_ok = messagebox.askokcancel(
            title=site, message=f"These are the details you entered:\nEmail: {mail}\nPassword: {pw}\n\nIs it ok to save?")
        if is_ok:
            with open(file="./password-generator/data.txt", mode="a") as f:
                f.write(f"{site} | {mail} | {pw}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#ui setup

window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=70)
# canvas
img = PhotoImage(file="./password-generator/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)
# labels
website_label = Label(text="Website:", font=("Arial", 9, "bold"))
website_label.grid(row=2, column=1, sticky="E")
username_label = Label(text="Email/Username:", font=("Arial", 9, "bold"))
username_label.grid(row=3, column=1, sticky="E")
password_label = Label(text="Password:", font=("Arial", 9, "bold"))
password_label.grid(row=4, column=1, sticky="E")
# entrys
website_entry = Entry(width=36)
website_entry.grid(row=2, column=2, columnspan=2, sticky="W")
website_entry.focus()
username_entry = Entry(width=36)
username_entry.grid(row=3, column=2, columnspan=2, sticky="W")
username_entry.insert(0, my_email)
password_entry = Entry(width=15)
password_entry.grid(row=4, column=2, sticky="W")
# buttons
password_button = Button(
    width=16, text="Generate Password", command=generate_pass)
password_button.grid(row=4, column=2, sticky="E", columnspan=2)

add_button = Button(width=30, text="Add", command=add_click)
add_button.grid(column=2, columnspan=2, row=5, sticky="W")


window.mainloop()
