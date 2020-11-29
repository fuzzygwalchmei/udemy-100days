#! /bin/python3

# # 3 Exercise 1 - Heads or Tails
import random

test_seed = int(input("Input a seed: "))
random.seed(test_seed)

random_side = random.rantint(0,1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")

# Exercise 2 - Bankers Roulette
print("Bankers roulette!")
namesAsCSV = input("Give me everybody's names, seperated by a comma: ")
names = namesAsCSV.split(',')

# pick = random.randint(0, len(names)-1)
pick = random.choice(names)
print(f"{pick.strip()} is paying for everything today!")

# Exercise 3 - Treasure Map
row1 = [".", ".", "."]
row2 = [".", ".", "."]
row3 = [".", ".", "."]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?: ")
x, y = int(position[0])-1, int(position[1])-1
map[x][y] = 'X'
print(f"{row1}\n{row2}\n{row3}")

# Exercise 4 - Rock Paper Scissors
options = {"rock":0, "paper":1, "scissors":2}
wins = [[0,1,2],
        [1,0,2],
        [2,1,0],
        [3,3,3]]
outcome = {0:"It was a draw", 1:"The player Wins!",2:"The computer Wins!",3:"The player made an invalid choice :("}
choice = input("Make your choice (rock, paper or scissors): ").lower()
player = (options.get(choice, 3))
comp = random.choice(list(options.keys()))
computer = options.get(comp)
print(f"Player chose: {choice} and Computer chose {comp}")
print(outcome.get(wins[player][computer]))
