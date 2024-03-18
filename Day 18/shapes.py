import turtle

timmy = turtle.Turtle()

colors = ["maroon", "red", "purple", "green", "olive", "yellow", "navy", "blue", "aqua"]


def draw_shape(num_sides):
    for sides in range(num_sides):
        timmy.color(colors[num_sides - 3])
        timmy.forward(100)
        timmy.left(360 / num_sides)


for sides in range(3, 110):
    draw_shape(sides)
