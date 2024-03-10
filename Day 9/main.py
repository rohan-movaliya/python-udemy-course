import art, os

print(art.logo)
print("\nWelcome to the secret auction program.")

auction_bid = {}
while True:
    name = input("What is your name? ")
    bid = int(input("What's your bid?  $"))
    auction_bid[name] = bid
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if restart == "no":
        os.system("cls")
        winner_bid = 0
        for key in auction_bid:
            if auction_bid[key] > winner_bid:
                winner_bid = auction_bid[key]
                winner_name = key
        print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
        break
    os.system("cls")
