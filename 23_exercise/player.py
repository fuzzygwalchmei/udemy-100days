from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.go_to_start()


    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finishline(self):
        return self.ycor() == FINISH_LINE_Y

    def turtle_up(self):
        self.forward(MOVE_DISTANCE)
        

    def turtle_down(self):
        self.backward(MOVE_DISTANCE)

    def turtle_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def turtle_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)
