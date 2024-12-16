from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.color("white")
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", font=("courier", 50, 'normal'))
