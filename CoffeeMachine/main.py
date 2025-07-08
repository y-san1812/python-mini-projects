MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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
money=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#check whether there are sufficient ingredients
def check_ingredients(drink,ingredient):
    if resources[ingredient] >= MENU[drink]["ingredients"][ingredient]:
        return True

    else:
        return False

#make the drink and borrow ingredients from resources
def make_drink(drink,ingredient):
    resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

def costings(drink):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    change=((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies*0.01))-MENU[drink]["cost"]
    if change<0:
        return False
    else:
        print(f"Here is ${round(change,2)} in change.")
        return True

# main code
def coffee_machine():
    global money

    sufficient_resources = True
    machine=True

    #prompt user
    user_inp=input("What would you like? (espresso/latte/cappuccino):")
    if user_inp=="off":
        machine=False

    if machine:

        #show the resources and money that is present in the machine
        if user_inp=="report":

            print(f'''Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${round(money,2)}
''')

        else:
                #inform user if ingredients aren't available
                for key in resources:
                    if not check_ingredients(user_inp,key):
                        sufficient_resources=False
                        print(f"Sorry, we don't have enough {key}")


                #make the drink and add the money provided by user
                if sufficient_resources:
                    if costings(user_inp):

                        money += MENU[user_inp]["cost"]
                        for key in resources:
                            make_drink(user_inp,key)
                        print(f"Here is your {user_inp}☕ Enjoy!")
                    else:
                        print("Sorry, you don't have enough money.")

        coffee_machine()

coffee_machine()



