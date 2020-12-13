#! /bin/python3 
# 
from random import choice, randint
from turtle import Turtle, Screen, colormode

directions = [0, 90, 180, 270]

timmy = Turtle()
colormode(255)
timmy.shape("turtle")
timmy.pensize(10)
timmy.speed("fastest")

def random_color():
    return (randint(0,255), randint(0, 255), randint(0, 255))


# # Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(270)

# # Draw a dashed line
# for _ in range(10):
#     timmy.forward(20)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.pendown()

# # Draw multiple shapes
# shapes = {"triangle":{"sides":3, "color":"red"},
#         "square":{"sides":4, "color":"blue"},
#         "pentagon":{"sides":5, "color":"green"}}

# for shape in shapes:
#     timmy.color(shapes[shape]["color"])
#     angle = 360/shapes[shape]["sides"]
#     sides = shapes[shape]['sides']

#     for _ in range(sides):
#         timmy.forward(50)
#         timmy.left(angle)

# Turle, Random Walk
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(choice(directions))



screen = Screen()
screen.exitonclick()