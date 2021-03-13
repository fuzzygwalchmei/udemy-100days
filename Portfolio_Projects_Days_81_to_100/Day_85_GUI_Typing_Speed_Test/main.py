from tkinter import Frame, Tk, Label, Entry, Button
from timeit import timeit
from typing import Collection


# import words from a file


# GUI

app = Tk()
text = ''

def key(event):
    global text
    text += event.char
    print(text)
    print(len(text))

# lbl_display = Label()

# ent_text = Entry()
# btn_start = Button(text="Start")
# btn_finish = Button(text="Finish")
# btn_restart = Button(text="Restart")
# Label to display words
# Highlight current word
# matching character to character, no reversed

# try again button
# something like speedtest?

frame = Frame(app, width=100, height=100)
frame.bind_all("<Key>",key)
frame.pack()
# lbl_display.grid(row=0, column=0, columnspan=3)
# ent_text.grid(row=1, column=0, columnspan=3)
# btn_start.grid(row=2, column=0)
# btn_finish.grid(row=2, column=1)
# btn_restart.grid(row=2, column=2)

# FEATURES

# words per minute
# accuracy
# mistakes
# difficulty levels





if __name__ == "__main__":
    app.mainloop()