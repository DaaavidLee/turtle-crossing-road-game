COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.generate_car()


    def generate_car(self):
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=3)
        self.penup()

        self.goto(random.randint(-270,270),random.randint(-250,270))
        self.color(COLORS[random.randint(0,5)])
        self.setheading(180)
        self.forward(STARTING_MOVE_DISTANCE)

    def accelerate(self):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)


