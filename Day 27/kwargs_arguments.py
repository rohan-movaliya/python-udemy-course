# def calculator(n,**numbers):
# type of numbers = dict
# print(numbers)
# for key,value in numbers.items():
#     print(f"{key} :- {value}")
# print(numbers["add"])

# n += numbers["add"]
# n *= numbers["multiply"]
# print(n)


# calculator(2,add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")  # same as dict["key"] value
        self.price = kw.get("price")


my_car = Car(make="Rohan", model="Python")
print(my_car.make)
print(my_car.model)
print(my_car.price)
