import pandas as pd

# 1. Create a dictionary in this format: {"A":"Alfa","B":"Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
phone_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word : ").upper()
output_list = [phone_dict[letter] for letter in word]
# output_list = [value for (key,value) in phone_dict.items() if key in word ]
print(output_list)
