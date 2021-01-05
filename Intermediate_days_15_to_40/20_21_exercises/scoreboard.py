#! /bin/python3

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.goto(0, 270)
            self.penup()
            self.color('white')
            self.update_scoreboard()
            self.hideturtle()

        def update_scoreboard(self):
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

        def increase_scoreboard(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()

        def game_over(self):
            self.goto(0,0)
            self.write("Game Over!", align=ALIGNMENT, font=FONT)
