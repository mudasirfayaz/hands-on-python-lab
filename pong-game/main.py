from turtle import Screen
import time
from scoreboard import Score
from ball import Ball
from paddle import Paddle
from constants import *

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()
score1 = Score(-70, 290)
score2 = Score(70, 290)
r_paddle = Paddle((670, 0))
l_paddle = Paddle((-670, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Wall bounce
    if ball.ycor() > 380 or ball.ycor() < -370:
        ball.bounce_vertical()

    # Paddle collisions
    if ball.distance(r_paddle) < 50 and ball.xcor() > 640:
        ball.bounce_horizontal()
        ball.move_speed *= BALL_SPEED_INCREMENT

    if ball.distance(l_paddle) < 50 and ball.xcor() < -640:
        ball.bounce_horizontal()
        ball.move_speed *= BALL_SPEED_INCREMENT

    # Miss detection
    if ball.xcor() > 680:
        ball.reset()
        score1.increment()

    if ball.xcor() < -680:
        ball.reset()
        score2.increment()

screen.exitonclick()
