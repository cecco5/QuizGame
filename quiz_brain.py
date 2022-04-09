
class QuizBrain:
    """Models the QuizBrain object"""
    def __init__(self, question_list):
        self.number = 0
        self.score = 0
        self.list = question_list

    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        user_answer = input(f"Q.{self.number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.number < len(self.list)

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"The current score is {self.score}/{self.number}.")
        print("\n")









