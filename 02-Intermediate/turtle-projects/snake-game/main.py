from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

REFRESH_RATE = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen to keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True

while game_running:
    screen.update()
    time.sleep(REFRESH_RATE)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend()
        scoreboard.increment_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_running = False
        scoreboard.display_game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.display_game_over()

screen.exitonclick()
