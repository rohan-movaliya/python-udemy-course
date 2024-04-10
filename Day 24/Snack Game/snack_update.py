from turtle import Screen
from snack import Snack
from food import Food
from score_board import ScorbBoard
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

# 1. Create a snack body
snack = Snack()

# 4. Detect collision with food
food = Food()

# 5. Create a scoreboard
score_board = ScorbBoard()

# 3. Control the snack
screen.listen()
screen.onkey(key="Up", fun=snack.up)
screen.onkey(key="Down", fun=snack.down)
screen.onkey(key="Left", fun=snack.left)
screen.onkey(key="Right", fun=snack.right)

is_on_game = True
while is_on_game:
    screen.update()
    sleep(0.3)

    # 2. Move the snack
    snack.move()

    # 4. Detect collision with food
    if snack.head.distance(food) < 15:
        food.refresh()
        # 5. Create a scoreboard
        score_board.increse_score()
        snack.extend_snack()

    # 6. Detect collision with wall
    if (
        snack.head.xcor() > 280
        or snack.head.xcor() < -280
        or snack.head.ycor() > 280
        or snack.head.ycor() < -280
    ):
        snack.reset()
        score_board.reset()

    # 7. Detect collision with tail
    for segment in snack.snacks[1:]:
        if snack.head.distance(segment) < 10:
            snack.reset()
            score_board.reset()

screen.exitonclick()
