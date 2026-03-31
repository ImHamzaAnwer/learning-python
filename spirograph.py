import random
import turtle

colors = ["#7FFFD4", "#008000", "#00FF7F", "#8B008B", "#FA8072", "#1E90FF"]
directions = ["left", "right"]
angles = [0, 90, 180, 270]

timmy = turtle.Turtle()
timmy.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.pencolor(random_color())


draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
