#! /bin/python3

from  game_data_14 import data
from game_logo_14 import logo, vs
import random
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(a, b):
    return "A" if a['follower_count'] > b['follower_count'] else "B"


def pose_question(a,b):
    print("This round we will question who has more followers between (A or B): ")
    print(f"A: {a['name']} who is a {a['description']} from {a['country']}")
    print(vs)
    print(f"B: {b['name']} who is a {b['description']} from {b['country']}")

# Main function
def main():
    # Loop through questions
    # Keep score of correctly guessed
    score = 0
    # on correct guess, compare successful answer option to new option
    while True:

        a = random.choice(data)
        b = random.choice(data)

        pose_question(a,b)
        answer = compare(a,b)
        choice = input("Enter your choice here (A or B): ").upper()
        clear()
        if choice == answer:
            print(f"Correct!")
            score +=1
        else:
            print("Sorry, you got it wrong!")
            break
    print(f"Your final score was {score}")
if __name__ == "__main__":
    main()