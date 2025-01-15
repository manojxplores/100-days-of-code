from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface(Tk):
    def __init__(self, q_list):
        super().__init__()
        self.quiz = QuizBrain(q_list)
        ques_num, ques_txt = self.quiz.next_question()

        self.config(bg=THEME_COLOR, width=350, height=500)
        self.canvas = Canvas(height=300, width=300)
        self.ques_text = self.canvas.create_text(150, 150, text=f"{ques_txt}", width=280, font=("arial", 20, "italic"))
        self.score = Label(text="Score: 0", foreground="white", bg=THEME_COLOR, font=("arial", 10, "italic"))
        self.score.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img, command=lambda: self.give_feedback("true"))
        self.true_btn.grid(row=2, column=0, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img, command=lambda: self.give_feedback("false"))
        self.false_btn.grid(row=2, column=1, pady=20)

        self.mainloop()

    def give_feedback(self, ans):
        if self.quiz.check_answer(ans):
            self.canvas.config(bg="green")
            self.score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            ques_num, ques_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=f"{ques_txt}.")
        else:
            self.canvas.itemconfig(self.ques_text, text=f"You've completed the quiz\n"
                                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")