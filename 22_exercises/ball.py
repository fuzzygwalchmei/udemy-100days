from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('circle')
        self.x_speed = 10
        self.y_speed = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_speed, self.ycor()+self.y_speed)

    def bounce_y(self):
        self.y_speed *= -1
    
    def bounce_x(self):
        self.x_speed *= -1
        self.move_speed *=0.9


    def hit_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()


