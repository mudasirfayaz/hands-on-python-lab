import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = list(input("Enter you name: ").upper())
phonetic_code = [phonetic_dict[letter] for letter in word]
print(phonetic_code)
