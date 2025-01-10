from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface(Tk):
    def __init__(self):
        super().__init__()

        self.config(bg=THEME_COLOR, width=350, height=500)
        self.canvas = Canvas(height=300, width=300)
        self.ques_text = self.canvas.create_text(150, 150, text="Question")
        self.score = Label(text="Score: {}", foreground="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img)
        self.true_btn.grid(row=2, column=0, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img)
        self.false_btn.grid(row=2, column=1, pady=20)
