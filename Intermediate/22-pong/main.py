import time
from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

pong = Pong()

r_score = ScoreBoard((60, 220))
l_score = ScoreBoard((-60, 220))

screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_over = False
while not game_over:
    time.sleep(0.03)
    screen.update()
    pong.forward(10)

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()

    if pong.distance(r_paddle) < 50 or pong.distance(l_paddle) < 50:
        pong.bounce_x()

    if pong.xcor() > 380:
        l_score.increase_score()
        pong.reset_position()

    if pong.xcor() < -380:
        r_score.increase_score()
        pong.reset_position()


screen.exitonclick()
