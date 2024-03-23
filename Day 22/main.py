from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

# 1. Create the screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# 2. Craete and move a paddle
r_paddle = Paddle((350, 0))

# 3. Create another paddle
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# 4. Create the ball and make it move
ball = Ball()

# 7. Key score
score_board = ScoreBoard()


game_is_one = True
while game_is_one:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # 5. Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # 6. Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()
