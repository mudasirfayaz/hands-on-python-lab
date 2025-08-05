from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

REFRESH_RATE = 0.1

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen to keyboard input for controlling the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True

# Main game loop
while game_running:
    screen.update()  # Update the screen manually
    time.sleep(REFRESH_RATE)  # Control the speed of the game
    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()  # Move food to a new random location
        snake.extend()  # Add a new segment to the snake
        scoreboard.increment_score()  # Increase the score

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        snake.reset()  # Reset the snake to starting position
        scoreboard.reset()  # Reset the score

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()  # Reset the snake to starting position
            scoreboard.reset()  # Reset the score

screen.exitonclick()  # Exit the game when the screen is clicked
