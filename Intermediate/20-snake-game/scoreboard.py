from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((0, 270))
        self.speed("fastest")
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("Game Over!", align=ALIGN, font=FONT)
