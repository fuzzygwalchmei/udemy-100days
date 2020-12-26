import tkinter as tk
from tkinter import Image, StringVar
from tkinter.constants import LEFT
from typing import Collection
from numpy.lib.function_base import flip
import pandas as pd
from PIL import ImageTk
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

# Try clause to see if this has been used before, otherwise use the default file
try:
    data = pd.read_csv("./data/remaining_words.csv")
except FileNotFoundError as e:
    data = pd.read_csv("./data/french_words.csv")
words = data.to_dict(orient="records")
print(len(words))
word = {'French':'commencer', 'English':'begin'}


def is_known():
    global word
    words.remove(word)
    get_word()


def get_word():
    """
    get a new french word
    """
    global flip_timer
    global word
    window.after_cancel(flip_timer)
    word = choice(words)
    can_front.itemconfig(card_image, image=img_front)
    can_front.itemconfig(card_title, text="French", fill="black")
    can_front.itemconfig(card_word, text=word['French'], fill="black")
    flip_timer = window.after(3000, translate)

def translate():
    """
    Function to flip the card to english version
    """
    global word
    can_front.itemconfig(card_image, image=img_back)
    can_front.itemconfig(card_title, text="English", fill="white")
    can_front.itemconfig(card_word, text=word['English'], fill="white")


    


window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, translate, word)

img_front = ImageTk.PhotoImage(file="./images/card_front.png")
img_back = ImageTk.PhotoImage(file="./images/card_back.png")
can_front = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_image = can_front.create_image(400,263, image=img_front)

# Text for flash card
card_title = can_front.create_text(400, 150, font=("Arial", 40, "italic"))
card_word = can_front.create_text(400, 300, font=("Arial", 60, "bold"))

# Bottom Buttons
img_right = ImageTk.PhotoImage(file="./images/right.png")
img_wrong = ImageTk.PhotoImage(file="./images/wrong.png")
btn_right = tk.Button(image=img_right, highlightthickness=0, command=is_known)
btn_wrong = tk.Button(image=img_wrong, highlightthickness=0, command=get_word)

# Pack everything via grid
can_front.grid(row=0, column=0, columnspan=2)
btn_wrong.grid(row=1, column=0)
btn_right.grid(row=1, column=1)


get_word()

window.mainloop()

data = pd.DataFrame(words)
data.to_csv('./data/remaining_words.csv', index=False)