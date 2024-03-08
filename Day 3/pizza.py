print("Welcom to My Python Code Pizza Deliveries")
size = input("What size pizza you want? (S, M, L)")
add_pepperoni = input("Do want to pepperoni? (Y or N)")
extra_cheese = input("Do want to add extra cheese? (Y or N)")
bill = 0

# Small Pizza : $15
# Medium Pizza : $20
# Large Pizza : $25

# pepperoni for small Pizza : +$2
# pepperoni for medium ot large Pizza : +$3

# extra cheese for any size pizza : +$1

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is ${bill}.")
