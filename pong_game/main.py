from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from padel import Padel
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

sccoreboard = Scoreboard()
l_padel = Padel(-380, 0)
r_padel = Padel(380, 0)
ball = Ball()


screen.listen()
screen.onkey(r_padel.move_up, "Up")
screen.onkey(r_padel.move_down, "Down")
screen.onkey(l_padel.move_up, "w")
screen.onkey(l_padel.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(r_padel) < 50
        and ball.xcor() > 340
        or ball.distance(l_padel) < 50
        and ball.xcor() < -340
    ):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        sccoreboard.update_r_score()

    if ball.xcor() < -380:
        ball.reset_position()
        sccoreboard.update_l_score()


screen.exitonclick()
