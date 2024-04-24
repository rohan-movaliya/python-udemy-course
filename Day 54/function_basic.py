def outer_function():
    print("I'm outer")

    def inner_function():
        print("I'm inner")

    return inner_function


nested_function = outer_function()  # I'm outer
nested_function()  # I'm inner
