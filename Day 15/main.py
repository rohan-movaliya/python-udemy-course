from data import resources,MENU
from art import logo

# function to print report
def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


# function to check resource sufficient or not
def is_report_sufficient(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    rest_resources = resources
    for key in drink_ingredients:
        if resources[key] < drink_ingredients[key]:
            print(f"Sorry there is not enough {key}.")
            return True


# function for udate resource
def update_resource(drink):
    drink_ingredients = MENU[drink]["ingredients"]
    for key in drink_ingredients:
        resources[key] -= drink_ingredients[key]
    resources["money"] += MENU[drink]["cost"]



# function for coins process
def coins_process(drink):
    print("Please insert coins")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    drink_price = MENU[drink]["cost"]
    change = round(total - drink_price,2)

    if total < drink_price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if total != 0:
            print(f"Here is ${change} dollars in change.")
        update_resource(drink)
        print(f"Here is your {drink} ☕️. Enjoy!")

machine_turn_on = True
print(logo)
while machine_turn_on:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        machine_turn_on = False
    elif order == "report":
        print_report()
    elif order in ["espresso", "latte", "cappuccino"]:
        if is_report_sufficient(order) == True:
            continue
        else:
            coins_process(order)
    else:
        print("Invalid Order. Try again!")
