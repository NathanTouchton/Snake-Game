from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed(0)
        self.goto(0, 270)

    def update_score(self, score_input):
        self.clear()
        self.write(f"Score: {score_input}", align="center", font=("Arial", 10))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Courier", 15))
