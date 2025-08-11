import time
from turtle import Screen
import random
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly create a new car
    if random.randint(1, 6) == 1:
        car_manager.create_car()

    car_manager.move_cars()

    if player.ycor() > FINISH_LINE_Y:
        player.reset()
        score.increment()
        car_manager.accelerate()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
