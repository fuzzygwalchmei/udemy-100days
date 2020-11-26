#! /bin/python3

# print('Hello World!')
# Part 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to say')")
print("print(\"what to say\")")

print("Hello World!\n"*3)
print("Hello","Marc")


# Part 2
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print("Hello "+input("What is your name?: "))


# Part 3
name = input("Enter your name: ")
name_len = len(name)
print(f"Your name {name} is {name_len} characters long")


a = input("a: ")
b = input("b: ")
print(f"a == {a}, and b == {b}")
b, a = a, b
print("switcheroo...")
print(f"Now... a == {a}, and b == {b}")

# Day 01 Project
print("Welcome o the Band Name Generator.")
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("Whats the name of your Pet?\n")

band_name = f'{city_name} {pet_name}'
print(band_name)