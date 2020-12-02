#! /bin/python3

word_list = ["aardvark", "baboon", "camel"]

from random import choice
chosen_word = choice(word_list)

display = ['_' for i in range(len(chosen_word))]

print(display)

guess = input("Pick a letter: ").lower()
print("It is" if guess in chosen_word else "Try again")