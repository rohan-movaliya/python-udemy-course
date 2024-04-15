fruits = ["Apple", "Pear", "Orange"]

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print(
            f"The list conatain only {len(fruits)} items. The index {index} is not in list."
        )
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
