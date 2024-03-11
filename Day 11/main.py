import art, os, random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# function to find winner
def blackjack_win(your_cards, comp_cards):
    # calculate score
    your_score = sum(your_cards)
    comp_score = sum(comp_cards)

    # adjust over score
    if your_score > 21 and 11 in your_cards:
        your_score -= 10
    if comp_score > 21 and 11 in your_cards:
        your_score -= 10

    # compare and find result
    if your_score > 21:
        return "You went over. You lose 😭"
    elif your_score == comp_score:
        return "Draw 🙃"
    elif comp_score > 21:
        return "Opponent went over. You win 😁"
    elif your_score > comp_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    # print logo
    print(art.logo)

    # give 2 cards and print
    your_cards = [random.choice(cards), random.choice(cards)]
    comp_cards = [random.choice(cards), random.choice(cards)]
    print(f"    Your cards : {your_cards}, current score : {sum(your_cards)}")
    print(f"    Computer's first card: {comp_cards[0]}")

    # set user cards
    is_add = True
    while is_add:
        add_more_cards = input("type 'y' to get another card, type 'n' to pass: ")
        if add_more_cards == "y":
            your_cards.append(random.choice(cards))
            print(f"    Your cards : {your_cards}, current score : {sum(your_cards)}")
            print(f"    Computer's first card: {comp_cards[0]}")
        else:
            is_add = False

    # set computer cards
    set_computer_score = True
    while set_computer_score:
        if sum(comp_cards) < 17:
            comp_cards.append(random.choice(cards))
        else:
            set_computer_score = False

    # print final result
    print(f"   Your final hand: {your_cards}, final score: {sum(your_cards)}")
    print(f"   Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
    print(blackjack_win(your_cards, comp_cards))


is_play = True
while is_play:
    is_play_again = input(
        "\nDo you want to play a game of Blackjack? Type 'y' or 'n': "
    )
    if is_play_again == "y":
        os.system("cls")
        play_game()
    else:
        is_play = False
