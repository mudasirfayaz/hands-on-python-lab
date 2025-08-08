from turtle import Turtle
import random
from constants import BALL_START_POS


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(BALL_START_POS)
        self.setheading(random.randint(20, 70))

    def reset(self):
        self.move_speed = 0.1
        self.goto(BALL_START_POS)
        self.setheading(self.heading() + 180)

    def move(self):
        self.forward(20)

    def bounce_vertical(self):
        self.setheading(360 - self.heading())

    def bounce_horizontal(self):
        self.setheading(180 - self.heading())
