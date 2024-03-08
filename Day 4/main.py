import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# for Art **https://ascii.co.uk/art**
options = [rock, paper, scissors]
you = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))
print("\nYour Choise")
print(options[you])

comp = random.randint(0, 2)
print("\nComputer Choise")
print(options[comp])

if you == comp:
    print("It's a Draw")
else:
    if you == 0:
        if comp == 1:
            print("You lose ")
        elif comp == 2:
            print("You Win")
    elif you == 1:
        if comp == 0:
            print("You Win")
        elif comp == 2:
            print("You lose")
    elif you == 2:
        if comp == 0:
            print("You lose")
        elif comp == 1:
            print("You win")
