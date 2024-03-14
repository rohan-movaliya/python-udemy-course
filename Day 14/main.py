import art, game_data, random, os


def get_random_account():
    return random.choice(game_data.data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_number(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(art.logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'Aa' or 'B': ").lower()
        a_followes_count = account_a["follower_count"]
        b_followes_count = account_b["follower_count"]
        is_correct = check_number(guess, a_followes_count, b_followes_count)

        os.system("cls")
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")


game()
