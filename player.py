from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color("red")
        self.showturtle()

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def turtle_reset(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

