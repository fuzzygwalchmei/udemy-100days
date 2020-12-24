import tkinter as tk
from tkinter import messagebox
from typing import Collection, Text
from PIL import ImageTk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from string import ascii_letters, digits, punctuation
from random import choice, choices, shuffle

def gen_password():
    ent_password.delete(0, tk.END)
    password_temp = []
    password_temp.extend(choices(ascii_letters, k=5))
    password_temp.extend(choices(digits,k=3))
    password_temp.extend(choices(punctuation, k=3))
    shuffle(password_temp)
    passwd = "".join(password_temp)
    ent_password.insert(0, passwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if not ent_website.get():
        messagebox.showerror(message="No Website entered")
    elif not ent_username.get():
        messagebox.showerror(message="No Username entered")
    elif not ent_password.get():
        messagebox.showerror(message="No Password entered")        
    else:
        with open('passwords.txt','a') as f:
            my_string = f"{ent_website.get()} | {ent_username.get()} | {ent_password.get()}\n"
            print(my_string)
            f.write(my_string)
        ent_website.delete(0, tk.END)
        ent_username.delete(0, tk.END)
        ent_password.delete(0, tk.END)
        messagebox.showinfo(message="Details stored")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=15, pady=15)
window.title("Password Manager")
canvas = tk.Canvas(width=200,height = 200)
img = ImageTk.PhotoImage(file="logo.png")
logo = canvas.create_image(100,100,image=img)

lbl_website = tk.Label(text="Website:")
ent_website = tk.Entry(width=40)

lbl_username = tk.Label(text="Email/Username:")
ent_username = tk.Entry(width=40)

lbl_password = tk.Label(text="Password")
ent_password = tk.Entry(width=21)
btn_password = tk.Button(text="Generate Password", command=gen_password)

btn_add = tk.Button(text="Add", width=35, command=add_password)

canvas.grid(row=0, column=1)
lbl_website.grid(row=1, column=0)
ent_website.grid(row=1, column=1, columnspan=2)

lbl_username.grid(row=2, column=0)
ent_username.grid(row=2, column=1, columnspan=2)

lbl_password.grid(row=3, column=0)
ent_password.grid(row=3, column=1)
btn_password.grid(row=3, column=2)

btn_add.grid(row=4, column=1, columnspan=2)












window.mainloop()