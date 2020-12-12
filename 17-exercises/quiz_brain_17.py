class QuizBrain(object):
    

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number<len(self.question_list)
    
    def check_answer(self, user_answer):
        if user_answer == self.question_list[self.question_number].answer:
            self.score += 1
            print("You got it right!")
        else:
            print(f"Sorry, you got it wrong, its actually {self.question_list[self.question_number].answer}")
        return user_answer == self.question_list[self.question_number].answer



    def next_question(self):
        user_answer = input(f"Q{self.question_number+1} {self.question_list[self.question_number].text} (True/False): ").capitalize()
        self.check_answer(user_answer)
        self.question_number += 1

        
        

