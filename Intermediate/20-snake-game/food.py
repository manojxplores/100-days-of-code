from turtle import Turtle
import random

HEIGHT = 260
WIDTH = 260


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("Blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.random_pos()

    def random_pos(self):
        x_corr = random.randint(-HEIGHT, HEIGHT)
        y_corr = random.randint(-WIDTH, WIDTH)
        self.goto((x_corr, y_corr))
