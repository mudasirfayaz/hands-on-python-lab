import string
from art import logo

letters = string.ascii_lowercase
alphabet = list(letters + letters)

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    while shift_amount > 26:
        shift_amount -= 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")
    print(" ")


run_again = True
while run_again:
    print(" ")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    try:
        shift = int(input("Type the shift number: "))
    except ValueError:
        print("Invaild shift number. Try again.")
        continue

    print(" ")

    caesar(text, shift, direction)

    restart = input("Type 'Yes' if you want to go again. Otherwise type 'No': ").lower()
    if restart == "no":
        run_again = False
        print("Goodbye")
