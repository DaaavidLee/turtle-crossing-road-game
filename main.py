import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

# player set up
player = Player()
screen.onkey(player.move, "Up")

# car set up
car = CarManager()

# scoreboard set up
scoreboard = Scoreboard()


# speed set up
init_speed = 0.1

# game functions
game_is_on = True
while game_is_on:
    time.sleep(init_speed)
    screen.update()
    car.generate_car()


    # level up
    while player.ycor() > 280:
        scoreboard.level_up()
        player.restart()
        car.accelerate()


    # game over
    while player.distance(car) < 35:
        game_is_on = False
        scoreboard.endgame()




screen.exitonclick()