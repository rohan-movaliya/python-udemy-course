import os, art


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation_function():
    print(art.logo)
    number1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("pick an operation from the line above: ")
        number2 = float(input("Enter the next number: "))
        calculation = operations[operation_symbol]
        answer = calculation(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        is_continue = input(
            f"type 'y' to continue calculating with {answer}, ot type 'n' to start a new calculation: "
        )
        print("\n")
        if is_continue == "y":
            number1 = answer
        else:
            continue_calculation = False
            os.system("cls")
            calculation_function()


calculation_function()
