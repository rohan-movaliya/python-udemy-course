from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snack:
    def __init__(self):
        self.snacks = []
        self.create_snack()
        self.head = self.snacks[0]

    def create_snack(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("circle")
        timmy.color("green")
        timmy.penup()
        timmy.goto(position)
        self.snacks.append(timmy)

    def reset(self):
        for snack in self.snacks:
            snack.goto(1000, 1000)
        self.snacks.clear()
        self.create_snack()
        self.head = self.snacks[0]

    def extend_snack(self):
        self.add_segment(self.snacks[-1].position())

    def move(self):
        for snack in range(len(self.snacks) - 1, 0, -1):
            new_x = self.snacks[snack - 1].xcor()
            new_y = self.snacks[snack - 1].ycor()
            self.snacks[snack].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
