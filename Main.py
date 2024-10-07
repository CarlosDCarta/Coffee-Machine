#***************************************************************************************************************************************
#Coffee Machine
#Carlos Cartagena
#10/6/2024
#Purpose take in user input to either print report or/and complete coffee transaction
#***************************************************************************************************************************************
import Coffee_Data

#functions
def checking_resources(coffee_ingred):
   for item in coffee_ingred:
        if coffee_ingred[item] > coffee_resources[item]:
            print(f"sorry there is not enough {coffee_ingred[item]}")
            return False
        else:
            return True
        
def using_resources(coffee_ingred):
    #updating the current stock level
    for key, value in coffee_ingred.items():
        coffee_resources[key] -= value
    return coffee_resources
#main program
menu = Coffee_Data.MENU
coffee_resources = Coffee_Data.resources

while True:
    #ask user for input and check it('report','coffee')
    user_input = input("What coffee would you like(Espresso, Latte, Cappuccino?): ").lower()
    # process secret word "off" for service of coffee machine. 
    if user_input == "off":
        quit()
    elif user_input == "report":
        print(coffee_resources)
    else:
        for key in menu:
            if key == user_input:
                coffee_ingred = menu[key]["ingredients"]
                coffee_price = menu[key]["cost"]

    #check if there is enough resoucres 
    result_of_check = checking_resources(coffee_ingred)
    if result_of_check != False:
        using_resources(coffee_ingred)
    # process user coins for transaction

    # Process resources used

    # repeat

