import random
import turtle

colors = ["#7FFFD4", "#008000", "#00FF7F", "#8B008B", "#FA8072", "#1E90FF"]
directions = ["left", "right"]
angles = [0, 90, 180, 270]

timmy = turtle.Turtle()
timmy.speed(6)
timmy.pensize(8)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for _ in range(100):
    timmy.forward(30)
    timmy.setheading(random.choice(angles))
    timmy.pencolor(random_color())


screen = turtle.Screen()
screen.exitonclick()
