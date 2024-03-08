import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
which_pay = names[random.randint(0, len(names) - 1)]

# which_pay = random.choice(names)

print(f"{which_pay} is going to buy the meal today!")
