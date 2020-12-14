#! /bin/python3
from turtle import Turtle, Screen, color, goto, window_height


s = Screen()
s.setup(width=500, height=400)

# def move_forward():
#     t.forward(10)

# def turn_left():
#     t.left(10)

# def turn_right():
#     t.right(10)

# def move_backwards():
#     t.back(10)

# def clear():
#     t.home()
#     t.clear()
    
# s.listen()
# s.onkey(move_forward, 'w')
# s.onkey(turn_left, 'a')
# s.onkey(turn_right, 'd')
# s.onkey(move_backwards,'s')
# s.onkey(clear, 'c')

y_positions = [-70, -40, -10, 20, 50, 80]
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'grey']
is_race = False

user_bet = s.textinput(title="Make your bet", prompt="Which turtle do you want to bet on")
all_turtles = []

for i in range(6):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    all_turtles.append(t)

if user_bet:
    is_race = True

from random import randint

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race = False
            if winning_color == user_bet:
                print("Congrats, you picked the winning turtle")
            else:
                print("You didnt pick the winner, better luck next time!")

        rand_dist = randint(1,10)
        turtle.forward(rand_dist)


s.exitonclick()
