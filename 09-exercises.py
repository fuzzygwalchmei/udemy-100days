#! /bin/python3

# Exercise 1 - Grading Program

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for k,v in student_scores.items():
    if v < 70:
        student_grades[k] = "Fail"
    elif v< 80:
        student_grades[k] = "Acceptable"
    elif v< 90:
        student_grades[k] = "Exceeds Expectation"
    else:
        student_grades[k] = "Outstanding"
print(student_grades)