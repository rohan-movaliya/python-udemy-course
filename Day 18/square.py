from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("arrow")
timmy.color("black")
timmy.pencolor("black")

for i in range(4):
    timmy.right(90)
    timmy.forward(100)

screen = Screen()
screen.exitonclick()
