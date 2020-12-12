#! /bin/python3

from dataclasses import dataclass
from data_file_15 import MENU, resources
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

available_resources = resources
available_resources['money'] = 0.00

commands = ['off', 'report']
commands.extend(MENU.keys())

# What would you like

# report: remaining resources and money
# choose drink
# insert coins (quantity of each)
# calculate change

# report insufficient resources before taking coins 
# calculate if enough coins we supplied
# check if transaction successful
# if not, dont subtract resources

# make coffee

#TODO: Print Resouces
def print_resources():
    print(f"Water: {available_resources['water']}ml")
    print(f"Milk: {available_resources['milk']}ml")
    print(f"Coffee: {available_resources['coffee']}g")
    print(f"Money: ${available_resources['money']:.2f}")


#TODO: Check for sufficient Resouces
    # To be done before processing coins
def check_resources(requested):
    available = []
    for each in requested.keys():
        available.append(requested[each] < available_resources[each])
        if not (requested[each] < available_resources[each]):
            print(f"Sorry, there is not enough {each}")
    return all(available)

# TODO: Process Coins
def get_money():
    quarters = int(input("How many Quarters: "))
    dimes = int(input("How many Dimes: "))
    nickels = int(input("How many Nickels "))
    pennies = int(input("How many Penniess: "))
    return (0.25*quarters)+(0.1*dimes)+(0.05*nickels)+(0.01*pennies)

def check_money(cost, money):
    return money > cost

    # To be done before making coffee
    # Calculate if enough money was provided
    # Calculate change

# TODO: Was the transaction successful
def make_coffee(order):
    global available_resources
    for each in order:
        available_resources[each] -= order[each]
    
    # Make coffee
    # reduce resource quantities
def update_resources(order, money):
    global available_resources
    for each in order['ingredients']:
        available_resources[each] -= order['ingredients'][each]
    available_resources['money'] += order['cost']
    change = money - order['cost']
    if change > 0:
        print(f"Heres your ${change:.2f} change")

# TODO: Commands == espresso, latte, cappucinno, off, report
def debug(order, available_resources, money_received):
    print(f"Order: {order}")
    print(f"Ingredients: {order['ingredients']}")
    print(f"Money Received: {money_received}")
    print_resources()

def main():

    while True:
        money_received = 0
        order = input("What would you like? (espresso/latte/cappucino): ")

        # debug(MENU[order], available_resources, money_received)
        item = MENU.get(order, order)
        # if order not in commands:
        if order not in commands:
            print("That is not a valid request")
        elif order == 'off':
            break
        elif order == 'report':
            print_resources()
        elif not check_resources(item['ingredients']):
            print("Not enough resources")

            print_resources()
        elif check_resources(item['ingredients']):
            # get_money
            money_received = get_money()
            if check_money(item['cost'], money_received):
                make_coffee(item['ingredients'])
                print(f"Heres your {order}")
                update_resources(item, money_received)
                print_resources()
            else:
                print("Sorry, thats not enough money. Money refunded")
            # transaction successful:
                # 
            # if check right amount
                # make coffee
                # provide change if available
            # else
                # not enough money    

    print("Powering Down...")


if __name__ == "__main__":
    main()