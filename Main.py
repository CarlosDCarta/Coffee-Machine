#***************************************************************************************************************************************
#Coffee Machine
#Carlos Cartagena
#10/6/2024
#Purpose take in user input to either print report or/and complete coffee transaction
#***************************************************************************************************************************************
import Coffee_Data

#functions
def checking_resources(coffee_ingred):
   for key in coffee_ingred:
        if coffee_ingred[key] > coffee_resources[key]:
            print(f"sorry there is not enough {key}")
            return False
        else:
            return True
        
def using_resources(coffee_ingred):
    #updating the current stock level
    for key, value in coffee_ingred.items():
        coffee_resources[key] -= value
    return coffee_resources

def process_coins():
    print("Please enter coins.")
    total = int(input("How many quarters: ")) * .25
    total += int(input("How many dimes?: ")) * .10
    total += int(input("How many nickles: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    if total < coffee_price:
        print(f"Insuffeicent funds. The price is ${coffee_price}")
        return False
    else:
        return total

#counting and returning change.
def return_change(total_coins, coffee_price, money_earned):
    leftover = total_coins - coffee_price
    leftover = round(leftover, 2)
    print(f"Your change {leftover}")
    money_earned += coffee_price
    return money_earned
    
#main program
menu = Coffee_Data.MENU
coffee_resources = Coffee_Data.resources
money_earned = 0

while True:
    #ask user for input and check it('report','coffee')
    user_input = input("What coffee would you like(Espresso, Latte, Cappuccino?): ").lower()
    
    # process secret word "off" for service of coffee machine. 
    if user_input == "off":
        quit()
    elif user_input == "report":
        print(f"The remaining resources are {coffee_resources} and the machine holds ${money_earned}.")
    else:
        for key in menu:
            if key == user_input:
                coffee_ingred = menu[key]["ingredients"]
                coffee_price = menu[key]["cost"]

        #Processing resoucres 
        result_of_check = checking_resources(coffee_ingred)
        if result_of_check != False:
            #process coins from user
            total_coins = process_coins()
            if total_coins != False:
                money_earned = return_change(total_coins,coffee_price, money_earned)
                updated_coffee_resources = using_resources(coffee_ingred)
            # give user change back to user
            
