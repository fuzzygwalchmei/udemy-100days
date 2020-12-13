#! /bin/python3 
# 
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")

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

# Draw multiple shapes
shapes = {"triangle":{"sides":3, "color":"red"},
        "square":{"sides":4, "color":"blue"},
        "pentagon":{"sides":5, "color":"green"}}

for shape in shapes:
    timmy.color(shapes[shape]["color"])
    angle = 360/shapes[shape]["sides"]
    sides = shapes[shape]['sides']

    for _ in range(sides):
        timmy.forward(50)
        timmy.left(angle)




screen = Screen()
screen.exitonclick()