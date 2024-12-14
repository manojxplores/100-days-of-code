from turtle import Turtle
import random

HEIGHT = 250
WIDTH = 250


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.shapesize(1, 1, 1)

    def random_pos(self):
        x_corr = random.randint(-HEIGHT, HEIGHT)
        y_corr = random.randint(-WIDTH, WIDTH)
        self.goto((x_corr, y_corr))
