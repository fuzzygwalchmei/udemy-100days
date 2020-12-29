THEME_COLOR = "#375362"

import tkinter as tk
from tkinter import font
from PIL import ImageTk
from quiz_brain import QuizBrain


class GUIInterface():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Trivia Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = tk.Label(text = "Score: 0", bg=THEME_COLOR, fg="white")

        self.cnv_question = tk.Canvas(width=300,height=350, bg='white')
        self.question_text = self.cnv_question.create_text(150, 150, text="PLACEHOLDER",
                                                            width=250, fill=THEME_COLOR, font=('Ariel', 20, 'italic'))
        self.img_true = ImageTk.PhotoImage(file='./images/true.png')
        self.img_false = ImageTk.PhotoImage(file='./images/false.png')
        self.btn_true = tk.Button(image=self.img_true, highlightthickness=0, bg=THEME_COLOR, command= self.true_press)
        self.btn_false = tk.Button(image=self.img_false, highlightthickness=0, bg=THEME_COLOR, command= self.false_press)

        self.lbl_score.grid(row=0, column=1)
        self.cnv_question.grid(row=1, column=0, columnspan=2, pady=50)
        self.btn_true.grid(row=2, column=0)
        self.btn_false.grid(row=2, column=1)


        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        self.cnv_question.config(bg="white")
        if self.quiz.still_has_questions():
            self.btn_true.config(state='active')
            self.btn_false.config(state='active')            
            self.lbl_score.config(text=f"Score: {self.quiz.score}")
            q_text =  self.quiz.next_question()
            self.cnv_question.itemconfig(self.question_text, text = q_text)
        else:
            self.cnv_question.itemconfig(self.question_text, text = "You have reached the end of the Quiz")
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')

    def true_press(self):
        self.btn_true.config(state='disabled')
        self.btn_false.config(state='disabled')
        self.answer_check(self.quiz.check_answer('True'))


    def false_press(self):
        self.btn_true.config(state='disabled')
        self.btn_false.config(state='disabled')
        self.answer_check(self.quiz.check_answer('False'))

    def answer_check(self, answer: bool):
        if answer:
            self.cnv_question.config(bg="green")
        else:
            self.cnv_question.config(bg="red")

        self.window.after(1000, self.get_next_question)
