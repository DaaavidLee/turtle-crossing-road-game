FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_number = 1
        self.level()

    def level(self):
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(f"Level: {self.level_number}", align="left", font=FONT)

    def level_up(self):
        self.level_number += 1
        self.clear()
        self.level()

    def endgame(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


