import turtle
import csv
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

coords = csv.reader("50_states.csv")
df = pd.read_csv("50_states.csv")

guess_state = screen.textinput(title="Guess the state!", prompt="Whats another states name?: ").capitalize()

print(df[df.state == guess_state])


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()