age = int(input("Enter your current age: "))
# assuem our whole age is 90

rest_year = 90 - age

rest_days = rest_year * 365
rest_weeks = rest_year * 52
rest_months = rest_year * 12

print(f"You have {rest_days} days, {rest_weeks} weeks, {rest_months} months left.")
