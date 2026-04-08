from turtle import Screen
import time
import turtle
from my_turtle import MyTurtle
from block import Block
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.listen()

# block = Block()
my_turtle = MyTurtle()
scoreboard = Scoreboard()

screen.onkey(my_turtle.move_forward, "Up")
screen.onkey(my_turtle.move_backward, "Down")


blocks = []
for _ in range(30):
    new_block = Block()
    blocks.append(new_block)


game_is_on = True
while game_is_on:
    for block in blocks:
        block.move()
        if my_turtle.distance(block) < 25:
            game_is_on = False
            scoreboard.game_over()

    if my_turtle.ycor() > 300:
        my_turtle.reset_position()
        scoreboard.level_up()

    time.sleep(0.05)
    screen.update()


screen.exitonclick()
