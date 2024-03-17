class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number - 1].answer
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was : {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def next_question(self):
        for question in self.question_list:
            self.question_number += 1
            ask_question = input(
                f"Q.{self.question_number}: {self.question_list[self.question_number-1].text} (True/False)? :"
            )
            self.check_answer(ask_question)
