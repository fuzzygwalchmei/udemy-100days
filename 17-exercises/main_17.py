#! /bin/python3

from data_17 import question_data
from question_model_17 import Question
from quiz_brain_17 import QuizBrain

question_bank = [Question(question['text'], question['answer']) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Thats all the questions: ")
print("Final Score: ")
print(F"You scored {quiz.score} out of {len(quiz.question_list)}")