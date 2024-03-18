import colorgram, turtle, random

# extract color
# colors =  colorgram.extract("image.jpg",30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))

color_list = [
    (202, 164, 110),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102),
]

turtle.colormode(255)
timmy = turtle.Turtle()
timmy.penup()
timmy.speed(100)
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_dot_count = 100

for dot_count in range(1, number_dot_count + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
