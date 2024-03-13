import random, art

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def check_answer(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}")
    else:
        if guess > answer:
            print("Too high, guess samller number.")
        else:
            print("Too low, guess bigger number.")


def set_difficulty():
    level = input("hoose a difficulty. Type 'easy' or 'hard':")
    if level == "hard":
        return HARD_LEVEL_TURN
    else:
        return EASY_LEVEL_TURN


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)
attempts = set_difficulty()
print(answer)  # extra line
guess = 0
while guess != answer:
    if attempts > 0:
        print(f"\nYou have {attempts} remaining to guess the number")
        guess = int(input("Make a guess: "))
        check_answer(guess, answer)
    else:
        print("You've run out of guesses, you lose")
        break

    attempts -= 1
