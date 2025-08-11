from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car.penup()
        y_cor = random.randint(-250, 250)
        new_car.goto(300, y_cor)
        new_car.setheading(180)
        self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
            # Optionally, remove or reset cars that go off-screen:
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)

    def accelerate(self):
        self.car_speed += MOVE_INCREMENT
