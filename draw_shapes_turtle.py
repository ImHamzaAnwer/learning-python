import random
from turtle import Turtle, Screen

colors = ["#7FFFD4", "#008000", "#00FF7F", "#8B008B", "#FA8072", "#1E90FF"]

timmy = Turtle()
timmy.shape("turtle")


def create_shape(num_of_lines):
    angle = 360 / num_of_lines
    for _ in range(num_of_lines):
        timmy.forward(100)
        timmy.right(angle)


for num in range(3, 9):
    timmy.color(random.choice(colors))
    create_shape(num)


screen = Screen()
screen.exitonclick()
