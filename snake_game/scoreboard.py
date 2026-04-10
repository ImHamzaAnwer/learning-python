from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        self.hideturtle()
        self.penup()
        self.goto(0, 210)
        self.read_high_score()
        self.update_scoreboard()

    def read_high_score(self):
        with open("snake_game/data.txt") as file:
            data = file.read()
            self.high_score = int(data)

    def write_high_score(self):
        self.high_score = self.score
        with open("snake_game/data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            "center",
            ("Arial", 16, "bold"),
        )

    def reset(self):
        if self.score > self.high_score:
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def make_score(self):
        self.score += 1
        self.update_scoreboard()
