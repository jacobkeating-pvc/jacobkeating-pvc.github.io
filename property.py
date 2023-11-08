# Name: Jacob Keating
# Prog Purpose: This program computes personal property tax on vehicles for a six month bill

import datetime
# Define tax rates
TAX_RATE = 0.042
RLF_RATE = 1/3


######## define program functions ########
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to calculate another vehicle? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False

def get_user_data():
    global val, eligible
    val = int(input("\nWhat is the cost of your vehicle: "))
    eligible = input("\nAre you eligible for tax relief (Y/N)? ")


def perform_calculations():
    global total, relief, tax
    tax = (val * TAX_RATE)/2
    if eligible.upper() == "Y":
        relief = tax * RLF_RATE
        total = tax - relief
    else: 
        total = tax

def display_results():
    line ='--------------------------------------------'
    moneyf = '>9,.2f'
    print(line)
    print('****** PERSONAL PROPERTY TAX 2nd HALF ******')
    print(line)
    print('Assessed value                   $ ' + format(val,moneyf))
    print('Full annual ammount owed         $ ' + format(tax,moneyf))
    if eligible.upper() == "Y":
        print('Relief                           $ ' + format(relief,moneyf))
    print('Total ammount due                $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

main()