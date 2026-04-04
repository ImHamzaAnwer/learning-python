from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(0, 210)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 16, "bold"))

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(
            "You hit a wall, Game Over !", False, "center", ("Arial", 15, "bold")
        )

    def make_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
