#! /bin/python3

from turtle import Screen, Turtle
from player import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
scoreboard = Scoreboard()

ball = Ball()


screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()    
    ball.move()

    if ball.hit_wall():
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()

screen.exitonclick()