# imported files
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# object assign to the classes
score_board = Scoreboard()
tim = Player()
car = CarManager()

# keyboard button listening
screen.listen()
screen.onkeypress(tim.move_turtle, "w")

# main while loop game repeatability
game_is_on = True
while game_is_on:
    time.sleep(car.time)
    screen.update()
    car.random_car()
    car.car_move()

    # detecting the collusion
    for cars in car.all_car:
        if tim.distance(cars) < 20:
            score_board.game_over()
            game_is_on = False

    # checking if the turtle crossed the road
    if tim.ycor() >= 290:
        score_board.score_add()
        tim.turtle_reset()
        car.time_increse()

# To stay the screen
screen.exitonclick()
