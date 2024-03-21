from turtle import Turtle, Screen

screen = Screen()
timmy = Turtle()


def move_forward():
    timmy.forward(20)


def move_backward():
    timmy.backward(20)


def counter_clockwise():
    # right
    timmy.right(10)


def clockwise():
    timmy.left(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
