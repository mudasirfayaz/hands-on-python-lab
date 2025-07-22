from config import (
    MENU,
    resources,
    coin_values,
)  # Import configuration data from external file

money = 0  # Tracks total money collected by the machine

while True:
    # Prompt user for their coffee choice
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # Allows the user to turn off the machine
    if user_input == "off":
        break

    # Print a resource report
    if user_input == "report":
        for resource in resources:
            unit = "g" if resource == "coffee" else "ml"
            print(f"{resource.title()}: {resources[resource]}{unit}")
        print(f"Money: ${money}")
        continue

    # Handle invalid menu choices
    if user_input not in MENU:
        print("Invalid choice. Try again.")
        continue

    # Extract the ingredients needed for the selected drink
    ingredients = MENU[user_input]["ingredients"]

    # Check if there are enough resources to make the drink
    can_make_coffee = True
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, not enough {ingredient}")
            can_make_coffee = False
            break  # Exit loop as soon as a shortage is found

    if not can_make_coffee:
        continue  # Skip rest of loop and re-prompt the user

    # Process coins input from the user
    print("Please insert coins")
    cash_received = 0
    for coins in coin_values:
        count = int(input(f"How many {coins}: "))
        cash_received += (
            count * coin_values[coins]
        )  # Convert to dollar value and add to total

    # Check if the user inserted enough money
    item_cost = MENU[user_input]["cost"]
    if cash_received < item_cost:
        print("Sorry that's not enough money. Money refunded.")
        continue  # Re-prompt user without making coffee

    # Calculate and give change if needed
    change = round(cash_received - item_cost, 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {user_input} ☕ Enjoy!")

    # Deduct the used resources from the machine’s inventory
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount

    # Add the payment to the machine’s money reserve
    money += item_cost
