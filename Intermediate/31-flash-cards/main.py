from tkinter import *
import pandas as pd
import random

df = pd.read_csv("data/french_words.csv")
words_dict = {row.French: row.English for (idx, row) in df.iterrows()}

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
hero_img = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="trove", font=("Arial", 60, "bold"))
canvas.grid(grow=0, column=1)


def gen_random_word(choice):
    random_word = random.choice(list(words_dict.keys()))
    canvas.itemconfig(word, text=random_word, fill="black")
    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(hero_img, image=card_front)
    window.after(5000, flip_card, random_word)


def flip_card(rand_word):
    print("Flipping the card...")
    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(hero_img, image=card_back)
    canvas.itemconfig(word, text=f"{words_dict[rand_word]}", fill="white")


right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=lambda: gen_random_word("right"))
right_btn.grid(row=1, column=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=lambda: gen_random_word("wrong"))
wrong_btn.grid(row=1, column=0)


window.mainloop()
