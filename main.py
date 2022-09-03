# TODO 1: Ask user what they want "espresso/latte/cappuccino"
# TODO 2: "off" turns the coffee machine off
# TODO 3: "report" shows resources & money made
# TODO 4: Check if resources are sufficient
# TODO 5: Process coins if resources are sufficient
# TODO 6: Check if transaction if successful: too little? too much? Add to profit
# TODO 7: Make coffee: subtract resources then hand over drink to user!

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


def generate_report(water_level, milk_level, coffee_level, money_made):
    """
    function returns formatted report of resources & money
    """
    print(f"Water: {water_level}ml\nMilk: {milk_level}ml\nCoffee: {coffee_level}g\nMoney: ${money_made}")


def coinage(beverage):
    """requests coin input, calculates if transaction was successful, displays any change,
    provides drink to user if applicable
    """

    print("Please insert coins.")
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickles = int(input("how many nickles?: "))
    num_pennies = int(input("how many pennies?: "))

    quarters = num_quarters * 0.25
    dimes = num_dimes * 0.10
    nickles = num_nickles * 0.05
    pennies = num_pennies * 0.01

    add_coins = quarters + dimes + nickles + pennies
    total_coins = round(add_coins, 2)
    print(f"Amount Received: ${total_coins}")

    if total_coins >= MENU[beverage]["cost"]:
        if total_coins > MENU[beverage]["cost"]:
            change = total_coins - MENU[beverage]["cost"]
            print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {beverage} ☕. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def service():
    """
    function starts the coffee machine requests based on customer input,
    calculates resources left & money made
    """
    water = 300
    milk = 200
    coffee = 100
    money = 0

    in_service = True
    while in_service:
        request = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        if request == "off":
            print("Coffee machine now off.")
            in_service = False
        elif request == "espresso" or request == "latte" or request == "cappuccino":
            if "water" in MENU[request]["ingredients"]:
                water -= MENU[request]["ingredients"]["water"]
            if "milk" in MENU[request]["ingredients"]:
                milk -= MENU[request]["ingredients"]["milk"]
            if "coffee" in MENU[request]["ingredients"]:
                coffee -= MENU[request]["ingredients"]["coffee"]
            if water < 0 or milk < 0 or coffee < 0:
                if water < 0:
                    print("Sorry there is not enough water.")
                if milk < 0:
                    print("Sorry there is not enough milk.")
                if coffee < 0:
                    print("Sorry there is not enough coffee.")
            else:
                transaction = coinage(request)
                if transaction != 0:
                    money += MENU[request]["cost"]
                else:
                    if "water" in MENU[request]["ingredients"]:
                        water += MENU[request]["ingredients"]["water"]
                    if "milk" in MENU[request]["ingredients"]:
                        milk += MENU[request]["ingredients"]["milk"]
                    if "coffee" in MENU[request]["ingredients"]:
                        coffee += MENU[request]["ingredients"]["coffee"]
                # print(f"Money: {money}")
        elif request == "report":
            generate_report(water, milk, coffee, money)
        else:
            print("Invalid Entry.")


service()

