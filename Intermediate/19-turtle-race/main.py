from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()

if user_input not in color_list:
    print("Provide valid input !")
    user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()

instances = []

y = -130
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(color_list[i])
    tim.penup()
    tim.goto(x=-230, y=y)
    y += 50
    instances.append(tim)

game_over = False
winner_idx = 0
while not game_over:
    for idx, turtle in enumerate(instances):
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            winner_idx = idx
            game_over = True

winning_color = color_list[winner_idx]
if winning_color == user_input:
    print(f"You win. The {winning_color} turtle is the winner!")
else:
    print(f"You lose. The {winning_color} turtle is the winner!")

screen.exitonclick()


