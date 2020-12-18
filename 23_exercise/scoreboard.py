from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, -280)
        self.hideturtle()
        self.message = f"Score: {self.level}"
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(self.message, align="left", font = FONT)

    
    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.message = 'GAME OVER'
        self.update_scoreboard()
