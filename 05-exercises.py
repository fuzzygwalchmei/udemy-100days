#! /bin/python3

# Exercise 01 - Average Height
# student_heights = [180, 124, 165, 173, 189, 169, 149]
student_heights = input("Input a list of student heights: ").split()
total = 0
count = 0
for height in student_heights:
    total+=int(height)
    count+=1

avg_height = total//count
print(f"The average height is {avg_height}")

# Exercise 2 - Highest score
student_scores = input("Input a list of student scores: ").split()
max = 0
for score in student_scores:
    if int(score) > max:
        max = int(score)
print(f"The hightest score was {max}")

# Exercise 3 - Adding even numbers
total = sum([x for x in range(101) if x%2 ==0])
print(total)

# Exercise 4 - FizzBuzz
for i in range(101):
    if i%15==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

# Exercise 5 - Password Generator
c_letters = int(input("How many letters would you like?: "))
c_symbols = int(input("How many symbols would you like?: "))
c_numbers = int(input("How many numbers would you like?: ")) 

password = []
import random
from string import ascii_letters, digits, punctuation
for char in range(c_letters+1):
    password.append(random.choice(ascii_letters))
for sym in range(c_symbols+1):
    password.append(random.choice(punctuation))
for num in range(c_numbers+1):
    password.append(random.choice(digits))

random.shuffle(password)
password = ''.join(password)
print(password)