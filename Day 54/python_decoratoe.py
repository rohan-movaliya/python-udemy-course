import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # somthing before function
        function()
        function()
        # something after function

    return wrapper_function


@delay_decorator
def hello():
    print("Hello!")


def greetings():
    print("How are you?")


@delay_decorator
def bye():
    print("Bye!")


# means of decorator
decorator_function = delay_decorator(greetings)
decorator_function()

# above two line code same as @delay_decorator
