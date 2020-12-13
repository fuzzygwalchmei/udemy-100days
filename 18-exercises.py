#! /bin/python3 
# 
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")

# Draw a square
for _ in range(4):
    timmy.forward(100)
    timmy.right(270)





screen = Screen()
screen.exitonclick()