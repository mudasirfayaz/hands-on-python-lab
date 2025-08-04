import random  # generating pseudo-random numbers
import string  # provides a collection of useful constants and classes for working with strings.


def generate_password(password_length, use_symbols):
    material = (
        string.ascii_letters + string.digits
    )  # string of all ascii letters (uppercase & lowercase) + digits (0-9)
    if use_symbols:
        material += string.punctuation  # adds special symbols (like !@#$&...)

    return "".join(random.choice(material) for _ in range(password_length))
    # create string of random characters picked from material as per password length


while True:
    try:
        print(" ")
        length = int(input("Enter the password length (8-32): "))
        symbols = input("Do you want to include symbols (Y/N): ").lower()
        if symbols == "y":
            use_symbols = True
        break
    except ValueError:
        print("Invalid input! Enter password length again (8-32): ")
        continue

password = generate_password(length, use_symbols)
print(f"Your password is: {password}")
print(" ")
