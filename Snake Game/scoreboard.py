from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 270)
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()

    def update_score(self, score_input):
        self.clear()
        self.score = score_input
        self.write(f"Score: {score_input} High Score: {self.high_score}", align="center", font=("Arial", 10))

    def reset_score(self):
        if self.score > int(self.high_score):
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()
        self.score = 0
