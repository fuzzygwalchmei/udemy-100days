#! /bin/python3

from random import randint




def gen_rand_number():
    return randint(1, 101)

def check_number(guess):
    return guess == num

def advise_user(guess):
        if guess < num:
            print("That guess was too low, try a higher number.\n")
        if guess > num:
            print("That guess was too high, try a lower number.\n")

num = gen_rand_number()

def main():
    finished = False
    guess = 0
    guesses = 0
    mode = input("Do you want to play easy (15 tries) or hard (5 tries)?: ")
    chances = 5 if mode == "hard" else 15
    while not finished and chances > guesses:
        try:
            guess = int(input(f"Please guess a number between 1 and 100 (guess {guesses}): "))
        except:
            print("Im going to guess you didnt enter a number")

        guesses += 1

        if guess not in range(1,101):
            print("That guess was outside of the range, its only between 1 and 100\n")
        elif check_number(guess):
            finished == True
            if guesses == 1:
                print("Wow, you guessed it on the first go!")
                break
            else:
                print(f"Congrats, you guessed the number in only {guesses} guesses!")
                break
        else:
            advise_user(guess)
    if not finished:
        print("Sorry, you didnt guess the number :(")



if __name__ == "__main__":
    main()
