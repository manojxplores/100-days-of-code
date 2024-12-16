from turtle import Turtle


class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.setheading(45)

    def bounce_y(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def bounce_x(self):
        new_heading = (180 - self.heading()) % 360
        self.setheading(new_heading)

    def reset_position(self):
        self.goto((0, 0))
        self.setheading(155)
