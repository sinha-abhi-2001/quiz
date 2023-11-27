class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        # TODO: 3. if quiz has ended
        return self.question_number < len(self.question_list)

    def next_question(self):
        curr_q_number = self.question_number
        curr_q = self.question_list[curr_q_number]
        # TODO: 1. asking the questions
        user_answer = input(f"Q. {curr_q_number + 1}: {curr_q.text} (True/False):  ")
        self.question_number += 1
        self.check_answer(user_answer, curr_q.answer)

    def check_answer(self, user_answer, correct_answer):
        # TODO: 2. checking if answer is right
        if user_answer.lower() == correct_answer.lower():
            print("You are right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")


