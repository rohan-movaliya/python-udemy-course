year = 2024

if year % 2 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap year.")
        else:
            print(f"{year} is not a Leap year.")
    else:
        print(f"{year} is a Leap year.")
else:
    print(f"{year} is not a Leap year.")
