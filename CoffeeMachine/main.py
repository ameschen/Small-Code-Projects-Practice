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

#TODO: Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.

drink = input("What would you like? (espresso/latte/cappuccino): ")


if drink == "off":
    exit()


#TODO: Print report.

if drink == "report":
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
    print("Money:")

#TODO: Check resources sufficient?

if drink == "espresso":




#TODO: Process coins.



#TODO: Check transaction successful?



#TODO: Make Coffee.

