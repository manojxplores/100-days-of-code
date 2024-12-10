import random
from game_data import data
from art import vs
import os


def render_data(acc):
    return f"{acc['name']}, a {acc['description']}, from {acc['country']}"


def compare(account1, account2):
    if account1["follower_count"] > account2["follower_count"]:
        return "A"
    else:
        return "B"


def higher_lower():
    game_over = False
    acc1 = random.choice(data)
    acc2 = random.choice(data)
    score = 0

    while not game_over:

        print(f"Compare A: {render_data(acc1)}")
        print(vs)
        print(f"Against B: {render_data(acc2)}")

        guess = input("Who has more followers? Type 'A' or 'B': ")
        while guess not in ["A", "B"]:
            print("Invalid input. Please type 'A' or 'B'.")
            guess = input("Who has more followers? Type 'A' or 'B': ")

        if guess == compare(acc1, acc2):
            score += 1
            os.system("cls")
            print(f"You're right! Current score: {score}")
            acc1 = acc2
            acc2 = random.choice(data)
            while acc2 == acc1:
                acc2 = random.choice(data)

        else:
            game_over = True
            os.system("cls")
            print(f"Sorry, that's wrong. Final score: {score}")


higher_lower()
