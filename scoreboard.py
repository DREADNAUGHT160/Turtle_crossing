from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"score:{self.score}", align="left", font=FONT)

    def score_add(self):
        self.score += 1
        self.clear()
        self.write(f"score:{self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(-70, 0)
        self.write("GAME OVER", align="left", font=FONT)


