import time
from turtle import Screen
from player import Player
from score_board import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

# 1. Move the turtle with keypress
player = Player()

screen.listen()
screen.onkey(key="Up", fun=player.up)

# 2. Create and move the car
car_manager = CarManager()

# 5. Create a scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # 3. Detect collsion with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 4. Detect when turtle reach the other side
    if player.is_at_finish_position():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
