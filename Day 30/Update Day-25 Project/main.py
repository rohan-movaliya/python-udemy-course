import pandas as pd

data = pd.read_csv("Update Day-25 Project/nato_phonetic_alphabet.csv")
phone_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word : ").upper()
    try:
        output_list = [phone_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabate please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
