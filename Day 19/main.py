from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)
is_race_on = False

user_bet = screen.textinput(title="Make Your Bat", prompt="Which turtle is win?")
color_list = ["yellow", "red", "orange", "green", "blue", "purple", "pink"]
y_position = [20, -10, 50, -40, 80, -70, 110]
all_turtle = []

for i in range(7):
    timmy = Turtle(shape="turtle")
    timmy.speed(2)
    timmy.color(color_list[i])
    timmy.penup()
    timmy.goto(x=-230, y=y_position[i])
    all_turtle.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner")
            else:
                print(f"You've losr! The {win_color} turtle is the winner")

        speed = random.randint(0, 10)
        turtle.forward(speed)


screen.exitonclick()
