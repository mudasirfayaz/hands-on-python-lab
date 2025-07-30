from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y = -100
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y)
    y += 40
    turtles.append(new_turtle)

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False

if user_bet == winner:
    print(f"You've won. The {winner} turtle is the winner!")
else:
    print(f"You've lost. The {winner} turtle is the winner!")

exit
