#***************************************************************************************************************************************
#Coffee Machine
#Carlos Cartagena
#10/6/2024
#Purpose take in user input to either print report or/and complete coffee transaction
#***************************************************************************************************************************************
import Coffee_Data

menu = Coffee_Data.MENU
coffee_resources = Coffee_Data.resources

#ask user for input and check it('report','coffee')
user_input = input("What coffee would you like(Expresso, Latte, Cappuccino?): ").lower
for key in menu:
    if key == user_input:
        print("coffee")
#check if there is enough resoucres 

#process user coins for transaction

#Process resources used

#repeat

#process secret word "off" for service of coffee machine. 