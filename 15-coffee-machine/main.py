MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def report(resource, money):
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink, resource):
    for key in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][key] > resource[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def process_coins(cost):
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25*quarters + 0.10*dimes + 0.05*nickels + 0.01*pennies
    if cost > total:
        print("Sorry that's not enough money. Money refunded.")
        return False, 0
    else:
        print(f"Here is ${round(total - cost, 2)} in change.")
        return True, cost


def make_coffe(drink, resource):
    for key in MENU[drink]["ingredients"]:
        resource[key] -= MENU[drink]["ingredients"][key]
    print(f"Here is your {drink}. Enjoy!")
    return resource


should_continue = True
while should_continue:
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input == "report":
        report(resources, money)
    elif user_input == "off":
        break
    else:
        if check_resources(user_input, resources):
            payment_successful, payment = process_coins(MENU[user_input]["cost"])
            if payment_successful:
                money += payment
                resources = make_coffe(user_input, resources)

