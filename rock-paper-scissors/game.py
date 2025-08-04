import random
import art

rock = art.rock
paper = art.paper
scissor = art.scissor

values = {0: rock, 1: paper, 2: scissor}


def play_game(users_choice, computers_choice):
    print(f"Your move: {values[users_choice]}\n")
    print(f"Computer's move: {values[computers_choice]}\n")

    if users_choice == computers_choice:
        print("Game Draw!")
        print(" ")
    elif users_choice == 2 and computers_choice == 0:
        print("You Lose!")
        print(" ")
    elif users_choice == 0 and computers_choice == 2:
        print("You Win!")
    elif users_choice > computers_choice:
        print("You Win!")
    elif users_choice < computers_choice:
        print("You Lose!")
        print(" ")


while input("Type 'y' to play game or type 'n' to quit: ").lower() == "y":
    users_choice = int(input("Type '0' for Rock, '1' for Paper or '2' for Scissor: "))
    computers_choice = random.randint(0, 2)

    if users_choice < 0 or users_choice > 2:
        print("Invalid Choice")
    else:
        play_game(users_choice, computers_choice)
