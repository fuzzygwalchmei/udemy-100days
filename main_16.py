#! /bin/python3

from menu_16 import Menu, MenuItem
from coffee_maker_16 import CoffeeMaker
from money_machine_16 import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()
menu = Menu()


def main():
    is_on = True
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like?: ({options})")

        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()