#! /bin/python3


digit = input("Type in a 2 digit number: ")
try:
    a = int(digit[0])
    b = int(digit[1])
    print(f'{a} + {b} = {a+b}')
except:
    print("Thats not a 2 digit number")


# BMI Calculator:
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

BMI = weight/height**2
print(f"Your BMI is {int(BMI)}")


# Day 2.3 Your life in weeks
age = int(input("What is your current age?: "))
years_left = 90 - age
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

# print(f"You have {days} days, {weeks} weeks, or {months} months left")

# Tip Calculator

print("Welcome to the Tip Calculator")
amount = float(input("Whats the amount to split: $"))
tip_perc = input("What percentage tip would you like to give? (10,12 or 15): ")
people = int(input("How many should this be split between?: "))

tip = float(f'1.{tip_perc}')
amount_tip = amount * tip
each = round(amount_tip/people, 2)

print(f"Each person should pay: ${each}")