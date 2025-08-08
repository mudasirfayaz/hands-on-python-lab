from turtle import Turtle
from constants import PADDLE_LIMIT


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def up(self):
        if self.ycor() < PADDLE_LIMIT:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -PADDLE_LIMIT:
            self.goto(self.xcor(), self.ycor() - 20)
