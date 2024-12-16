from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setpos(pos)
        self.speed("fast")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
