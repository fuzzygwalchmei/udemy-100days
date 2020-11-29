#! /bin/python3

# # Exercise 01
# print("welcome to the rollercoaster!")
# height = int(input("What is your height in cm?: "))

# if height > 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age?:"))
#     if age <12:
#         print("Your ticket will be $5")
#     elif age<=18:
#         print("Your ticket will be $7")
#     else:
#         print("Your ticket will be $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# # Challenge 1 - Odd and Even
# number = int(input("Which number do you want to check?: "))

# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# # Exercise 2 - Leap year
# year = int(input("Which year do you want to chec?: "))
# if year%400 == 0:
#     print("Leap Year")
# elif year%100 ==0:
#     print("Not a leap year")
# elif year%4==0:
#     print("Leap Year")
# else:
#     print("Not a leap year")

# Exercise 3.4 - Pizza Order
base = {'S':(15,2,1),'M':(20,2,1),'L':(25,3,1)}
total = 0

print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? (S,M or L): ")
add_pepperoni = input("Do you want Pepperoi? (Y or N): ")
extra_cheese = input("Do you want extra Cheese? (Y or N): ")

total += base.get(size.upper(),(15,0,0))[0]
if add_pepperoni.upper()=='Y':
    total += base.get(size.upper(),(15,0,0))[1]
if extra_cheese.upper()=='Y':
    total += base.get(size.upper(),(15,0,0))[2]

print(f"Your final bill is ${total}")