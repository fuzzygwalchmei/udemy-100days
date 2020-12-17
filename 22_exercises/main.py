#! /bin/python3

from turtle import Screen, Turtle


def go_up():
    player_1.goto(player_1.xcor(), player_1.ycor()+20)

def go_down():
    player_1.goto(player_1.xcor(), player_1.ycor()-20)

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

player_1 = Turtle()
player_1.shape("square")
player_1.color("white")
player_1.shapesize(stretch_len=1, stretch_wid=5)
player_1.penup()
player_1.goto(350,0)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()