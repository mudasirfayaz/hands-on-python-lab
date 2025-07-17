import operator

# Mapping of symbols to actual functions
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# Formats a number to an integer if it's a whole number, otherwise keeps it as a float.
def formatted_input(num):
    return int(num) if num == int(num) else num

def calculator():   
    # Infinite loop to keep the calculator running until the user decides to exit
    while True: 
        try:
            num1 = float(input("Enter first no: ")) 
        except ValueError: 
            print("Invalid input. Please enter numbers only.")
            print(" ")
            continue

        # Inner loop to prompt for operator until a valid one is entered
        while True:
            opr = input("Enter operation (+ - * /): ")

            if opr not in operations:
                print("Invalid operator. Try again.")
                print(" ")
                continue

            while True:
                try: 
                    num2 = float(input("Enter second no: "))
                    print(" ")
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    print(" ")
                    continue
                
            if num2 == 0 and opr == "/": # Prevent division by zero
                print("Division by zero is not allowed")
                print(" ")
                continue # Restart the inner loop
            
            formatted_num1 = formatted_input(num1)
            formatted_num2 = formatted_input(num2)
    
            result = round(operations[opr](formatted_num1, formatted_num2), 2)
            print(f"{formatted_num1} {opr} {formatted_num2} = {result}")
            print(" ")

            # Ask user if they want to perform another calculation
            choice = input(
                f"Type 'c' to continue calculating with {round(result, 2)}.\n"
                "Type 's' to start a new calculation.\n"
                "Type 'q' to quit: "
            ).lower()
            print(" ")
            if choice == "c":
                num1 = result  # Set result as first number and loop continues
            elif choice == "s": # Restart full calculator loop
                break  # Break to the outer loop to restart
            elif choice == "q":
                print("Good Bye!\n")
                return
            else:
                print("Invalid choice. Please enter 'c', 's', or 'q'.\n")

calculator()