from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Current score
        with open("snake-game/data.txt") as data:
            self.high_score = int(data.read())  # Highest score achieved
        self.color("white")
        self.penup()
        self.goto(-220, 250)  # Position the scoreboard
        self.hideturtle()
        self.update_display()  # Display the initial score

    def update_display(self):
        self.clear()  # Clear previous score display
        self.write(
            f"Score: {self.score}\nHigh Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )  # Write the current and high score

    def reset(self):
        # Update high score if current score is greater
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake-game/data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0  # Reset current score
        self.update_display()  # Update the display

    def increment_score(self):
        self.score += 1  # Increase score by 1
        self.update_display()  # Update the display
