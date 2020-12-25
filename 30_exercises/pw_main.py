from json.decoder import JSONDecodeError
import tkinter as tk
from tkinter import messagebox
from typing import Collection, Text
from PIL import ImageTk
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from string import ascii_letters, digits, punctuation
from random import choice, choices, shuffle
import pyperclip

PASSWORD_FILE = "passwords.json"

def gen_password():
    ent_password.delete(0, tk.END)
    password_temp = []
    password_temp.extend(choices(ascii_letters, k=5))
    password_temp.extend(choices(digits,k=3))
    password_temp.extend(choices(punctuation, k=3))
    shuffle(password_temp)
    passwd = "".join(password_temp)
    ent_password.insert(0, passwd)
    pyperclip.copy(passwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    if not ent_website.get():
        messagebox.showerror(message="No Website entered")
    elif not ent_username.get():
        messagebox.showerror(message="No Username entered")
    elif not ent_password.get():
        messagebox.showerror(message="No Password entered")        
    else:
        new_data = {ent_website.get():{
                    "email": ent_username.get(),
                    "password":ent_password.get()}}

        try:
            with open(PASSWORD_FILE,'r') as f:
                data = json.load(f)
        except JSONDecodeError as e:
            messagebox.showerror(message="No Such file exists")
            data={}
        finally:
            data.update(new_data)
            with open(PASSWORD_FILE,'w') as f:
                json.dump(data, f, indent=4)

            ent_website.delete(0, tk.END)
            ent_username.delete(0, tk.END)
            ent_password.delete(0, tk.END)
            messagebox.showinfo(message="Details stored")

def website_search():
    try:
        with open('passwords.json','r') as f:
            data = json.load(f)
            messagebox.showinfo(message=f"Details for {ent_website.get()} are:\n{data.get(ent_website.get(),'Not Entered')}")
    except JSONDecodeError as e:
        messagebox.showerror(message="There is no password file as yet")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=15, pady=15)
window.title("Password Manager")
canvas = tk.Canvas(width=200,height = 200)
img = ImageTk.PhotoImage(file="logo.png")
logo = canvas.create_image(100,100,image=img)

lbl_website = tk.Label(text="Website:")
ent_website = tk.Entry(width=40)
btn_search = tk.Button(text="Search", command=website_search)

lbl_username = tk.Label(text="Email/Username:")
ent_username = tk.Entry(width=40)

lbl_password = tk.Label(text="Password")
ent_password = tk.Entry(width=21)
btn_password = tk.Button(text="Generate Password", command=gen_password)

btn_add = tk.Button(text="Add", width=35, command=add_password)

canvas.grid(row=0, column=1)
lbl_website.grid(row=1, column=0)
ent_website.grid(row=1, column=1)
btn_search.grid(row=1, column=2)

lbl_username.grid(row=2, column=0)
ent_username.grid(row=2, column=1, columnspan=2)

lbl_password.grid(row=3, column=0)
ent_password.grid(row=3, column=1)
btn_password.grid(row=3, column=2)

btn_add.grid(row=4, column=1, columnspan=2)












window.mainloop()