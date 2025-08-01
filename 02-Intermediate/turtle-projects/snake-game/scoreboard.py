from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_display()

    def update_display(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_display()

    def display_game_over(self):
        self.goto(0, 0)
        self.color("Red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
