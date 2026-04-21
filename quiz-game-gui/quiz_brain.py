import html


class QuizBrain:
    def __init__(self, list):
        self.score = 0
        self.question_number = 0
        self.question_list = list
        self.current_question = None

    def still_have_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        unescaped_q = html.unescape(self.current_question.text)
        self.question_number += 1
        return unescaped_q

    def is_answer_right(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
