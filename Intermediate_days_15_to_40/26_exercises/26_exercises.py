doubled = [x*2 for x in range(1,5)]
print(doubled)

# Exercise 1 - Squared Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

# Exercises 2 - Even numbers
even_numbers = [x for x in numbers if x%2==0]
print(even_numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
from random import randint

student_scores = {student:randint(1,100) for student in names}
passed = {k:v for k, v in student_scores.items() if v > 50}
print(passed)

# Exercises 3 - Unladen Swallow
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

