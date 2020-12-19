#! /bin/python3


from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

screen.update()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    if -280 > snake.head.xcor() or snake.head.xcor() > 280 or -280 > snake.head.ycor() or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

scoreboard.reset()

screen.exitonclick()