# age : int
# name : str
# height : float
# is_human : bool  #declare variable with data type


def police_check(age: int) -> bool:  # declare parameter and return type with data type
    if age < 18:
        can_drive = True
    else:
        can_drive = False
    return 15


ans = police_check(18)
print(ans)


# This type of writing not work in VSCode, but it's highlight our error in other IDE like PyCharm
