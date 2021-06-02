from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#creating a class of CarManger
class CarManager:

    def __init__(self):
        self.all_car = []
        self.time = 0.1

    # To create random car(turtle)
    def random_car(self):
        random_choice = random.randint(1, 6)
        ran_y = random.randrange(-240, 260, 20)
        if random_choice == 6:
            new_car = Turtle()
            new_car.penup()
            new_car.goto(300, ran_y)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            self.all_car.append(new_car)

    # To move the car forward
    def car_move(self):
        for car in self.all_car:
            car.forward(STARTING_MOVE_DISTANCE)

    # To decrease the time of sleeping
    def time_increse(self):
        self.time *= 0.9
