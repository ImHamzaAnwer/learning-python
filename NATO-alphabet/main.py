import pandas as pd

data = pd.read_csv("NATO-alphabet/nato_phonetic_alphabet.csv")

words_dict = {row.letter: row.code for _, row in data.iterrows()}

user_input = input("Enter Your name: ").upper()

nato = [words_dict[letter] for letter in user_input]

print(nato)
