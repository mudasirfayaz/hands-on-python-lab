from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")  # Set the fastest animation speed
        self.refresh_position()  # Place the food at a random position

    def refresh_position(self):
        # Move the food to a new random position within the game boundaries
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        # Avoid spawning food in the top-left corner where it may be inaccessible
        if x < -150 and y > 220:
            x, y = x + 130, y - 60

        self.goto(x, y)  # Move the food to the new position
