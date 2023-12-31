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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(x):
    for ingredient in x:
        print(ingredient)


off = False
while off:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    drink.lower()
    for item in MENU:
        if item == drink:
            drinkChoice = item

            check_resources(drinkChoice)

        else:

            break

    if drink == "report":
        print("report")
    elif drink == "off":
        off = True
    else:
        print("Invalid input  please , please try again")

