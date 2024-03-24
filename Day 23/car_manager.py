from turtle import Turtle
import random

COLOURS = ["red", "yellow", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCRIMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.cat_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            new_car.goto(300, random.randint(-200, 200))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.cat_speed)

    def level_up(self):
        self.cat_speed += MOVE_INCRIMENT
