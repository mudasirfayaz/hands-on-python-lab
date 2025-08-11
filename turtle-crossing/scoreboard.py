from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increment(self):
        self.clear()
        self.level += 1
        self.update()

    def game_over(self):
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.write("GAME OVER", align="center", font=FONT)
