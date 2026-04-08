import random
from turtle import Turtle

COLORS = ["orange", "blue", "purple", "gray", "green"]


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 2)
        self.random_x_pos = random.randint(-300, 300)
        self.random_y_pos = random.randint(-240, 300)
        self.goto(self.random_x_pos, self.random_y_pos)

    def move(self):
        self.backward(5)
        if self.xcor() < -300:
            # self.shapesize(1, random.randint(3, 8))
            self.goto(300, random.randint(-240, 300))
