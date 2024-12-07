import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
    return turns


def compare(user_input, random_num):
    if user_input > random_num:
        print("Too high.")
        return True
    elif user_input < random_num:
        print("Too low.")
        return True
    else:
        print(f"You got it! The answer is {random_num}")
        return False


def play_game():
    num = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_choice = int(input("Make a guess: "))
        result = compare(user_choice, num)
        if result:
            attempts -= 1
            print('Guess again')
        else:
            return

    print(f"You've run out of guesses. The correct number was {num}. Better luck next time!")


play_game()