#! /bin/python3

word_list = ["aardvark", "baboon", "camel"]

from random import choice
chosen_word = choice(word_list)


lives = 5
heart = u'\u2764'
guesses = []
 

while lives > 0:
    display = [letter if letter in guesses else '_' for letter in chosen_word]
    print(display)
    if '_' not in display:
        print("You guessed the word!")
        break

    print(f"Lives: {lives*heart}")
    guess = input("Pick a letter: ").lower()
    if guess in guesses:
        print("You've already guessed that, pick again")    
    elif guess in chosen_word:
        guesses.append(guess)
    else:
        guesses.append(guess)
        lives -= 1
print("You lose! :(")

