import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
user_input = input("Enter a word: ").upper()
word_list = [nato_dict[letter] for letter in user_input if letter in nato_dict.keys()]
print(word_list)
