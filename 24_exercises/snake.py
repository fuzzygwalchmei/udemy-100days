from turtle import Turtle, Screen

START_POS = [0,-20,-40]
MOVE_DIST = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class segment(Turtle):
    def __init__(self):
        super().__init__()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


class Snake(object):
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in START_POS:
            self.add_segment((i,0))

    def add_segment(self, position):
        segment_new = Turtle('square')
        segment_new.penup()
        segment_new.color('white')
        segment_new.goto(position)
        self.snake.append(segment_new)

    def extend(self):
        self.add_segment(self.snake[-1].position())


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


    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)

        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]