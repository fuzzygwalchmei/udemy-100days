#! /bin/python3

# # Exercise 1 Functions with Outputs
# def format_name(f_name, l_name):
#     return f"{f_name.title()} {l_name.title()}"

# print(format_name("MaRC", "falZON"))

# def is_leap_year(year):
#     if year%400 == 0:
#         return True
#     elif year%100 ==0:
#         return False
#     elif year%4==0:
#         return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     days = month_days[month-1]
#     if is_leap_year(year) and month ==2:
#         days +=1
#     return days


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Exercise 2 - Calculator

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a//b

def calculator():
    repeat = "y"
    func = {"+":add, "-":sub, "*":mult, "/":div}

    result = int(input("What is the first value: "))
    while repeat == "y":
        a = result
        choice = input("Which operator (+,-,*,/): ")
        op = func.get(choice,add)
        b = int(input("What is the second number: "))
        result = op(a,b)
        print(f"{a} {choice} {b} = {result}")
        repeat = input("Do you want to more or restart? (y/n/r): ").lower()
        if repeat == "r":
            calculator()

calculator()

    