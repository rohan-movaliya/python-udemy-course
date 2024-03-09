import math


def paint_calc(height, width, cover):
    no_of_cans_required = math.ceil((height * width) / 5)
    print(f"You'll need {no_of_cans_required} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
