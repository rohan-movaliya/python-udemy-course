print("Welcome to Love Calculaor")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
count_TRUE = 0
count_Love = 0

myname = name1.lower()
mywifename = name2.lower()
total = myname + mywifename

count_TRUE += total.count("t")
count_TRUE += total.count("r")
count_TRUE += total.count("u")
count_TRUE += total.count("e")

count_Love += total.count("l")
count_Love += total.count("o")
count_Love += total.count("v")
count_Love += total.count("e")

love_score = int(str(count_TRUE) + str(count_Love))
print(love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score},  you are alright together.")
else:
    print(f"Your score is {love_score}.")
