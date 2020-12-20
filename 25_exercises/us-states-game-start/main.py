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



all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess_state = screen.textinput(title="Guess the state!", prompt="Whats another states name?: ").title()

    if guess_state == 'Quit':
        diff = set(all_states).difference(set(guessed_states))
        missed = pd.DataFrame(set(all_states).difference(set(guessed_states)))
        missed.to_csv("missed_states.csv")
        break

    elif guess_state in all_states:
        guessed_states.append(guess_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == guess_state]
        df[df.state == guess_state]['guessed'] = True
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())



def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)


turtle.mainloop()