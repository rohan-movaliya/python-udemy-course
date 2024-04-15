def add(*numbers):
    # type of numbers = tuple
    print(numbers[1])
    sum = 0
    for num in numbers:
        sum += num
    print(sum)


add(1, 2, 3, 4, 5)
