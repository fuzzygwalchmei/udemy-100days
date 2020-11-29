#! /bin/python3

# # 3 Exercise 1 - Heads or Tails
import random

# test_seed = int(input("Input a seed: "))
# random.seed(test_seed)

# random_side = random.rantint(0,1)

# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

# # Exercise 2 - Bankers Roulette
# print("Bankers roulette!")
# namesAsCSV = input("Give me everybody's names, seperated by a comma: ")
# names = namesAsCSV.split(',')

# # pick = random.randint(0, len(names)-1)
# pick = random.choice(names)
# print(f"{pick.strip()} is paying for everything today!")

# # Exercise 3 - Treasure Map
# row1 = [".", ".", "."]
# row2 = [".", ".", "."]
# row3 = [".", ".", "."]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure?: ")
# x, y = int(position[0])-1, int(position[1])-1
# map[x][y] = 'X'
# print(f"{row1}\n{row2}\n{row3}")