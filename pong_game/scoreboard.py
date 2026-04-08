from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def create_line(self):
        self.goto(0, 0)
        self.setheading(90)
        self.forward(280)
        self.setheading(270)
        self.pendown()
        for _ in range(28):
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))
        self.create_line()

    def update_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.update_scoreboard()
