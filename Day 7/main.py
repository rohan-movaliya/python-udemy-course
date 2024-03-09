import art, words, random

# print game logo
print(art.logo)

# chosen random word
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)


# make guess string
guess_string = []
for i in range(word_length):
    guess_string.append("_")
print(f"{guess_string} --> {word_length}\n\n")

end_of_game = False
lives = 6

while not end_of_game:

    # take guess from user
    print(
        "x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x==x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x=x"
    )

    # keep track on lives
    if lives == 0:
        print("\n\n**************** 👎 👎 You Lose 👎 👎 ****************")
        end_of_game = True
        break

    user_guess = input("\n\nGuess a letter: ").lower()

    # check the user have already guess or not
    if user_guess in guess_string:
        print("You have already Guess this words.")

    # According to guess, update the string
    for position in range(word_length):
        chosen_word_char = chosen_word[position]
        if chosen_word_char == user_guess:
            guess_string[position] = chosen_word_char

    # if user guess wrong, update the live
    if user_guess not in chosen_word:
        lives -= 1
        print("\n**************** 🥺 🥺 You lose your Life 🥺 🥺 ****************")

    # print lives stages
    print(art.stages[lives])

    # check guess string is fullfill or not
    if "_" not in guess_string:
        end_of_game = True
        print("**************** 👑 👑 You Win 👑 👑 ****************")

    # print guessing string
    print(" ".join(guess_string), "\n")
