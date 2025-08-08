from turtle import Turtle
from constants import *

ALIGNMENT = "center"
FONT = ("Courier", 64, "normal")


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.hideturtle()
        self.display()

    def increment(self):
        self.score += 1
        self.display()

    def display(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
