import turtle
import random

timmy = turtle.Turtle()
timmy.shape("arrow")
timmy.pensize(15)

directions = [0, 90, 180, 270]
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]

# def random_colrous():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     color = (r,g,b)
#     return color

for _ in range(200):
    timmy.speed(random.randint(1, 10))
    timmy.color(random.choice(colours))
    # timmy.color(random_colrous())
    timmy.forward(50)
    timmy.setheading(random.choice(directions))
