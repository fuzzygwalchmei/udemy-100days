from turtle import Turtle, Screen

START_POS = [0,-20,-40]
MOVE_DIST = 20

UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
class Snake(object):
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in START_POS:
            segment_new = Turtle('square')
            segment_new.penup()
            segment_new.color('white')
            segment_new.goto(i,0)
            self.snake.append(segment_new)


    def move(self):
        for i in range(len(self.snake)-1, 0, -1):
            self.snake[i].goto(self.snake[i-1].position())
        self.snake[0].forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
