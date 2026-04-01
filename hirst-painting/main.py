# import colorgram
import turtle
import random

# colors = colorgram.extract("hirst-painting/image.jpg", 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_colors.append((r, g, b))

# print(rgb_colors)

color_list = [
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

turtle.colormode(255)
jimmy = turtle.Turtle()
jimmy.penup()
jimmy.goto(-250, -200)


def create_row():
    for _ in range(1, 11):
        jimmy.dot(20, random.choice(color_list))
        jimmy.forward(50)


for num in range(1, 11):
    create_row()
    numb = num * 50
    jimmy.goto(-250, -200 + numb)


screen = turtle.Screen()
screen.exitonclick()
