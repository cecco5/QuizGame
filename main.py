from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question bank

bank = []
for question in question_data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    bank.append(Question(question_text, question_answer))


quiz = QuizBrain(bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz.")
print(f"The final score is {quiz.score}/{quiz.number}.")


























