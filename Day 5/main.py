import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the password generator !")
letter = int(input("How many letters would you like in your password?\n"))
symbol = int(input("How many symbols would you like in your password?\n"))
number = int(input("How many number would you like in your password?\n"))

# Eazy Level
password = ""
for i in range(1, letter + 1):
    password += random.choice(letters)
for i in range(1, number + 1):
    password += random.choice(numbers)
for i in range(1, symbol + 1):
    password += random.choice(symbols)

# Hard Level
# password = list(password)
# random.shuffle(password)
# password = "".join(password)
password = "".join(random.sample(password, len(password)))
# sample() in python

print(f"Here is your password : {password}")
