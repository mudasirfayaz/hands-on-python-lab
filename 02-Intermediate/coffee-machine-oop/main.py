from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")

    if user_input == "off":
        break
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    drink = menu.find_drink(user_input)
    if drink is None:
        continue

    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
        drink.cost
    ):
        coffee_maker.make_coffee(drink)
