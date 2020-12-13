#! /bin/python3 
# 
from random import choice, randint
from turtle import Turtle, Screen, colormode
import colorgram

directions = [0, 90, 180, 270]


colors = colorgram.extract("hirst.jpeg",20)
rgb_colors = [(c.rgb.r, c.rgb.b, c.rgb.g) for c in colors]


timmy = Turtle()
colormode(255)
timmy.shape("turtle")
# timmy.pensize(10)
timmy.speed("fastest")

# def random_color():
#     return (randint(0,255), randint(0, 255), randint(0, 255))


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

# # Turle, Random Walk
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(choice(directions))


# # Spiraograph
# for _ in range(72):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.setheading(timmy.heading() + 5)


# Drawing the Dots
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
for _ in range(10):

    for _ in range(10):
        timmy.setheading(0)    
        timmy.dot(20, choice(rgb_colors))
        timmy.forward(50)
        timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)


screen = Screen()
screen.exitonclick()