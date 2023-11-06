# Name: Jacob Keating, Afsana Nawrozi, Gabe Dyer
# Prog Purpose: This program computes cost of pizza and other products for a pizza restaurant

import datetime
# Define tuition & fee rates
PR_SMALL = 9.99
PR_MEDIUM = 12.99
PR_LARGE = 17.99
PR_EXTRA_LARGE = 21.99
PR_DRINK = 3.99
PR_BREAD = 6.99
RATE_TAX = 0.055

# global variables

numdrink = 0
numbread = 0


######## define program functions ########
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order more pizza? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False
            print("Thank you for ordering from Palermo Pizza Restaurant!")

def get_user_data():
    line ='----------------------------------------------'
    moneyf = '>11,.2f'
    print(line)
    print('********* PALERMO PIZZA COMPANY MENU *********')
    print(line)
    print("Pizza  S     SMALL               $ " + format(PR_SMALL,moneyf))
    print("Pizza  M     MEDIUM              $ " + format(PR_MEDIUM,moneyf))
    print("Pizza  L     LARGE               $ " + format(PR_LARGE,moneyf))
    print("Pizza  X     EXTRA LARGE         $ " + format(PR_EXTRA_LARGE,moneyf))
    print("Drink:                           $ " + format(PR_DRINK,moneyf))
    print("Order of Breadsticks:            $ " + format(PR_BREAD,moneyf))
    print(line)
    global pisize, numbread, numdrink, numpizza
    pisize = input("\nWhat is the size of the pizza you wish to order (S, M, L, X)?: ")
    numpizza = int(input("Number of pizzas: "))
    dr_yesno = input("Would you like order drinks with your pizza? (Y/N)? ")
    if dr_yesno.upper() == "Y":
        numdrink = int(input("Number of drinks: "))
    br_yesno = input("Would you like order breadsticks with your pizza? (Y/N)? ")
    if br_yesno.upper() == "Y":
        numbread = int(input("Number of breadsticks: "))

def perform_calculations():
    global picost, drcost, brcost, tax, total, subtotal
    if pisize.upper() == "S":
        picost = PR_SMALL * numpizza

    elif pisize.upper() == "M":
        picost = PR_MEDIUM * numpizza

    elif pisize.upper() == "L":
        picost = PR_LARGE * numpizza

    elif pisize.upper() == "X":
        picost = PR_EXTRA_LARGE * numpizza
    
    drcost = PR_DRINK * numdrink
    brcost = PR_BREAD * numbread

    subtotal = picost + drcost + brcost
    tax = subtotal * RATE_TAX
    total = tax + subtotal

def display_results():
    line ='---------------------------------------------'
    moneyf = '>6,.2f'
    print(line)
    print('*********** PALERMO PIZZA COMPANY ***********')
    print(line)
    print('Number of Pizzas                     # ' + format(numpizza,'>6,'))
    print('Cost of Pizzas                       $ ' + format(picost,moneyf))
    if numdrink > 0:
        print('Drink Cost                           $ ' + format(drcost,moneyf))
    if numbread > 0:
        print('Breadstick Cost                      $ ' + format(brcost,moneyf))
    print('Sales Tax                            $ ' + format(tax,moneyf))
    print('Subtotal                             $ ' + format(subtotal,moneyf))
    print('Total                                $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

main()