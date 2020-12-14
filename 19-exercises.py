#! /bin/python3
from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forward():
    t.forward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def move_backwards():
    t.back(10)

s.listen()
s.onkey(move_forward, 'w')
s.onkey(turn_left, 'a')
s.onkey(turn_right, 'd')
s.onkey(move_backwards,'s')


s.exitonclick()
