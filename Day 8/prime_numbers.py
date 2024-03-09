def prime_checker(number):
    if number > 1:
        check = True
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                check = False

        if check:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
