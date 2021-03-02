from tkinter import Tk, Label, Entry, Button, filedialog

app = Tk()

app.title("Image Watermarker")


def callback():
    name = filedialog.askopenfile()
    ent_file.config(text=name)

lbl_file = Label(text='Select File: ')
ent_file = Label()
btn_file = Button(text='Choose File', command=callback)
btn_submit = Button(text='Submit')

lbl_file.pack()
ent_file.pack()
btn_file.pack()
btn_submit.pack()


if __name__ == "__main__":
    app.mainloop()