import random

levels = {"easy": [50, 10], "medium": [75, 6], "hard": [100, 3]}


def difficulty():

    while True:
        level = input("Select a level (Easy/Medium/Hard): ").lower()
        if level not in levels:
            print("Invalid selection. Try again.")
            continue
        while True:
            print(" ")  # new line
            num = random.randint(1, levels[level][0])
            attempts_left = levels[level][1]

            while True:
                print(
                    f"Attempts left = {attempts_left}"
                )  # will show how many attempts are left
                print(" ")
                try:
                    guess = int(
                        input(f"Guess the number between 1 to {levels[level][0]}: ")
                    )  # user has to guess the number b/w the given range
                    print(" ")
                except ValueError:
                    print("Enter a valid number. Try again.")
                    print(" ")
                    continue

                # will check if the number matches the guess or not
                if guess > num:
                    print("Too High")
                    attempts_left -= (
                        1  # will decrement the number of attempts by 1 after each loss
                    )
                elif guess < num:
                    print("Too Low")
                    attempts_left -= 1
                else:
                    print("You won 🎉")  # if guess = number
                    print(" ")
                    break

                if attempts_left == 0:  # will check if no attempts are left
                    print("You lost 🥲")  # if yes user will lost the game
                    print(f"The number is {num}")
                    print(" ")
                    break  # will stop the inner loop

            choice = input(
                "Type 'g' to guess again. \nType 'c' to change level. \nType 'q' to quit: "
            ).lower()
            print(" ")
            if choice == "g":
                continue
            elif choice == "c":
                break
            else:
                print("Good Bye!")
                print(" ")
                return


difficulty()
