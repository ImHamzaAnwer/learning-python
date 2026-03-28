resources = {"water": 300, "milk": 200, "coffee": 100}
profit = 0

menu = {
    "latte": {"cost": 10, "ingredients": {"water": 100, "milk": 50, "coffee": 10}},
    "capuccino": {"cost": 15, "ingredients": {"water": 150, "milk": 80, "coffee": 25}},
    "espresso": {"cost": 8, "ingredients": {"water": 5, "milk": 10, "coffee": 30}},
}


def check_resources(ingredients):
    """Returns True if ingredients are sufficient otherwise returns False"""
    for resource in resources:
        if resources[resource] < ingredients[resource]:
            print(f"sorry there is not enough {resource}")
            return False
    return True


def calculate_total_coins():
    """Returns the total of all coins"""
    total = int(input("how many quarters? :")) * 0.25
    total += int(input("how many dimes? :")) * 0.10
    total += int(input("how many nickels? :")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total


closed = False

while not closed:
    choice = input("What would you like ? espresso, latte or capuccino: ")

    if choice == "report":
        print(f"water: {resources["water"]} ml")
        print(f"milk: {resources["milk"]} ml")
        print(f"coffee: {resources["coffee"]} g")
        print(f"money: ${profit}")
    elif choice == "latte" or choice == "capuccino" or choice == "espresso":
        if check_resources(menu[choice]["ingredients"]):

            print("please insert coins")
            total = calculate_total_coins()

            orderPrice = menu[choice]["cost"]
            if total >= orderPrice:
                profit += orderPrice
                print("Your coffee is ready")
                for item in resources:
                    resources[item] -= menu[choice]["ingredients"][item]

                if total > orderPrice:
                    change = round(total - orderPrice, 2)
                    print(f"here's your change back: {change}")
            else:
                print("Sorry that's not enough money")
    elif choice == "off":
        closed = True
