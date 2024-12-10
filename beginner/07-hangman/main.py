import random
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
guessed_word = []
for char in chosen_word:
    guessed_word.append("_")

print(chosen_word, guessed_word)

lives = 6
game_over = False

while not game_over:
    print(f"Word to guess: {''.join(guessed_word)}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_word:
        print(f"You've already guessed {guess}")
        continue

    if guess in chosen_word:
        for index, char in enumerate(chosen_word):
            if guess == char:
                guessed_word[index] = guess
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print(''.join(guessed_word))
    print(stages[lives])
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    if lives == 0:
        print(f"****************************IT WAS {chosen_word}! YOU LOSE****************************")
        game_over = True

    if "_" not in guessed_word:
        print("You win!")
        game_over = True

