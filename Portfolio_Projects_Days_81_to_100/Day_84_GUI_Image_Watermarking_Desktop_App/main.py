from tkinter import Tk, Label, Entry, Button, filedialog
from PIL import Image, ImageDraw, ImageFont

app = Tk()

app.title("Image Watermarker")


def transparency():
    edit_file = ent_file.cget("text")
    base_img = Image.open(edit_file)

    working_img = ImageDraw.Draw(base_img)
    black = (3, 8, 12)
    working_img.text((0,0), ent_text.get(), fill=black)
    rename = edit_file.split('.')
    rename[0] = f'{rename[0]}_watermarked'
    base_img.save('.'.join(rename))



def callback():
    name = filedialog.askopenfile()
    ent_file.config(text=name.name)

lbl_file = Label(text='Select File: ')
ent_file = Label()
btn_file = Button(text='Choose File', command=callback)
lbl_text = Label(text="Text for watermark")
ent_text = Entry()

btn_submit = Button(text='Submit', command=transparency)

lbl_file.pack()
ent_file.pack()
btn_file.pack()
ent_text.pack()
btn_submit.pack()


if __name__ == "__main__":
    app.mainloop()