import random
from hangman_words import word_list
from hangman_art import stages, logo, win, lose

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
hint = random.choices(chosen_word, k=3)

end_of_game = False
lives = 6

print(f"Hint: {''.join(hint)}")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word, You lose a life")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    print(stages[lives])

    if lives == 0:
        end_of_game = True
        print(lose)

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(win)
