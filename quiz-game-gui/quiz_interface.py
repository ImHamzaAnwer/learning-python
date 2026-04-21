from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=30, pady=30)

        self.score_label = Label(text=f"score: 0", font=("Courier", 18, "normal"))
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=500, height=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.question_text = self.canvas.create_text(
            250,
            150,
            text="hahahah",
            width=450,
            fill="black",
            font=("Arial", 26, "normal"),
        )

        true_image = PhotoImage(file="quiz-game-gui/images/true.png")
        false_image = PhotoImage(file="quiz-game-gui/images/false.png")

        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            borderwidth=0,
            command=lambda: self.get_answer("true"),
        )
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            borderwidth=0,
            command=lambda: self.get_answer("false"),
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        print(self.quiz.question_number)
        self.canvas.config(self.canvas, bg="white")
        self.score_label.config(text=f"score: {self.quiz.score}")
        if self.quiz.still_have_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz has ended")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def get_answer(self, user_answer):
        is_right = self.quiz.is_answer_right(user_answer)
        self.give_feedback(is_right)
        self.window.after(1000, self.get_next_question)

    def give_feedback(self, is_right):
        color = "green" if is_right else "red"
        self.canvas.config(bg=color)
