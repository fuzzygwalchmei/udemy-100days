#! /bin/python3

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 24, "normal")

class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            with open("data.txt") as hs:
                self.high_score = int(hs.read())
            self.goto(0, 270)
            self.penup()
            self.color('white')
            self.update_scoreboard()
            self.hideturtle()

        def update_scoreboard(self):
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

        def increase_scoreboard(self):
            self.score += 1
            self.update_scoreboard()

        def reset(self):
            if self.score > self.high_score:
                self.high_score = self.score

            
                
            self.score = 0
            self.update_scoreboard()

        def write_high_score(self):
            with open("data.txt", 'w') as hs:
                hs.write(f"{self.high_score}")
