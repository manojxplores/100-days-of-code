from turtle import Turtle, Screen
import pandas as pd

pointer = Turtle()
pointer.hideturtle()
pointer.penup()
pointer.speed("fastest")

states_img = "blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game")
screen.bgpic(states_img)

df = pd.read_csv("50_states.csv")
df['state'] = df['state'].str.lower()
states_list = df['state'].to_list()
guessed_states = []

score = 0
game_over = False
while not game_over:
    guess = screen.textinput(f"{score}/{len(states_list)} States Correct", "What's another states name?").lower()
    if guess == "exit":
        with open("states_to_learn.txt", mode="w") as file:
            for state in states_list:
                if state not in guessed_states:
                    file.write(f"{state}\n")
        break
    if guess in states_list:
        if guess in guessed_states:
            screen.textinput("Duplicate Guess", "You've already guessed that state! Try again.")
            continue
        score += 1
        guessed_states.append(guess)
        x_cor = df[df["state"] == guess].x.item()
        y_cor = df[df["state"] == guess].y.item()
        pointer.goto((x_cor, y_cor))
        pointer.write(f"{guess}", align="center", font=("Arial", 10, "bold"))
    else:
        screen.textinput("Invalid Guess", "That's not a valid state name! Try again.")

    if len(guessed_states) == len(states_list):
        screen.textinput("Congratulations!", "You've guessed all the states!")
        game_over = True

screen.exitonclick()

