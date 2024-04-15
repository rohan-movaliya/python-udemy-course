height = float(input("Height(m): "))
weight = float(input("Weight(kg): "))

if height > 3:
    # own exception
    raise ValueError("Human height should not be over than 3 meter.")

BMI = weight / height**2
BMI = round(BMI, 2)
print(f"BMI : {BMI}")
