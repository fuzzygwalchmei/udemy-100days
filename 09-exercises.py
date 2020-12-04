#! /bin/python3

# # Exercise 1 - Grading Program

# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62
# }

# student_grades = {}

# for k,v in student_scores.items():
#     if v <= 70:
#         student_grades[k] = "Fail"
#     elif v<= 80:
#         student_grades[k] = "Acceptable"
#     elif v<= 90:
#         student_grades[k] = "Exceeds Expectation"
#     else:
#         student_grades[k] = "Outstanding"
# print(student_grades)

# # Exercise 2 - Dictionary in List

# def add_new_country(country, visits, cities):
#     travel_log.append({"country":country, "visits": visits, "cities": cities})
#     print(f"You've vistied {country} {visits} times")
#     print(f"You've been to {' and '.join(cities)}")

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]        
#     }
# ]

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])


# Exercise 3 - Silent Auction
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bids = {}
more = "y"
max_bid = ['n/a',0]
while more =="y":
    clear()
    name = input("What is your name: ")
    bid = int(input("What is your bid?: "))
    bids[name] = bid
    more = input("Does someone else need to have a go?(y or n): ")

print(bids.items())
for k, v in bids.items():
    if v > max_bid[1]:
        max_bid = [k, v]

print(f"The highest bidder was {max_bid[0]} with a bid of {max_bid[1]}")



