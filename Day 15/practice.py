dict1 = {
    "water": 200,
    "milk": 150,
    "coffee": 24,
}

dict2 = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

for key in dict1:
    if dict1[key] <= dict2[key]:
        print("YES", key)
    else:
        print("NO", key)
