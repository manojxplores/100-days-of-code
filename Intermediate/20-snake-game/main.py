from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        score_board.update_score()
        food.random_pos()
        snake.add_segment()

    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or
            snake.segments[0].ycor() < -280):
        score_board.game_over()
        game_over = True

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 5:
            score_board.game_over()
            game_over = True


screen.exitonclick()

