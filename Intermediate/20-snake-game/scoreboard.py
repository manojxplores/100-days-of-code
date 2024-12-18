from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((0, 270))
        self.speed("fastest")
        with open("data.txt") as score_file:
            self.high_score = int(score_file.read())
        self.score = 0
        self.show_score()

    def update_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.show_score()
