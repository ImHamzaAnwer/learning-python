from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0, -280)

    def move_forward(self):
        y = self.ycor() + 10
        self.goto(0, y)

    def move_backward(self):
        y = self.ycor() - 10
        self.goto(0, y)

    def reset_position(self):
        self.goto(0, -300)
