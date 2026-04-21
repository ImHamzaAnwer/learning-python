from question_model import Question
from quiz_brain import QuizBrain
from quiz_interface import QuizInterface
import requests

response = requests.get(
    "https://opentdb.com/api.php", {"amount": 10, "type": "boolean"}
)
response.raise_for_status()
data = response.json()["results"]
question_bank = []
for question in data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    question_bank.append(Question(question_text, question_ans))


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
