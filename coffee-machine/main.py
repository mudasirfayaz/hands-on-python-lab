from config import (
    MENU,
    resources,
    coin_values,
)  # Import configuration data from external file

profit = 0  # Tracks total profit collected by the machine


def print_report():
    """Prints a resource and profit report."""
    for resource in resources:
        unit = "g" if resource == "coffee" else "ml"
        print(f"{resource.title()}: {resources[resource]}{unit}")
    print(f"Money: ${profit}")


def enough_resources(ingredients):
    """Returns True if there are enough resources to make the drink."""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, not enough {item}")
            return False
    return True


def process_coins():
    """Prompts user to insert coins and returns total calculated value."""
    print("Please insert coins")
    cash_received = 0
    for coins in coin_values:
        count = int(input(f"How many {coins}: "))
        cash_received += count * coin_values[coins]
    return cash_received


def make_coffee(drink_name, ingredients):
    """Deducts the required ingredients and serves the coffee."""
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount
    print(f"Here is your {drink_name} ☕ Enjoy!")


while True:
    # Prompt user for their coffee choice
    user_input = (
        input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
    )

    if user_input == "off":  # Allows the user to turn off the machine
        break
    elif user_input == "report":
        print_report()
        continue

    # Handle invalid menu choices
    if user_input not in MENU:
        print("Invalid choice. Try again.")
        continue

    # Extract the ingredients needed for the selected drink
    drink_ingredients = MENU[user_input]["ingredients"]

    # Check if there are enough resources to make the drink
    if not enough_resources(drink_ingredients):
        continue  # Skip rest of loop and re-prompt the user

    # Process coins input from the user
    payment = process_coins()

    # Check if the user inserted enough money
    item_cost = MENU[user_input]["cost"]
    if payment < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        continue  # Re-prompt user without making coffee

    # Calculate and give change if needed
    change = round(payment - item_cost, 2)
    print(f"Here is ${change} in change.")

    # Add the payment to the machine’s money reserve
    profit += item_cost

    # Make coffee & dispense the drink
    make_coffee(user_input, drink_ingredients)
