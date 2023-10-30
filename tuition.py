# Name: Jacob Keating
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
# PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# Define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# Define global variables 
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

######## define program functions ########
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to calculate tuition & fees for another student? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE: enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = int(input("Enter scholarship amount: "))

def perform_calculations():
    global total, balance, ituition, otuition, instition_fee, activity_fee, capital_fee
    ituition = RATE_TUITION_IN * numcredits
    otuition = RATE_TUITION_OUT * numcredits
    instition_fee = RATE_INSTITUTION_FEE * numcredits
    activity_fee = RATE_ACTIVITY_FEE * numcredits
    capital_fee = RATE_CAPITAL_FEE * numcredits
    if inout == 1:
        total = ituition + instition_fee + activity_fee
        balance = scholarshipamt-(ituition + instition_fee + activity_fee)
    elif inout == 2:
        total = otuition + instition_fee + activity_fee + capital_fee
        balance = scholarshipamt-(otuition + instition_fee + activity_fee + capital_fee)

def display_results():
    line ='---------------------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** PIEDMONT VIRGINIA COMMUNITY COLLEGE ****')
    print(line)
    if inout == 1:
        print('Tuition Amount                   $ ' + format(ituition,moneyf))
    elif inout == 2:
        print('Tuition Amount                   $ ' + format(otuition,moneyf))
    print('Institution Fee                  $ ' + format(instition_fee,moneyf))
    print('Activity Fee                     $ ' + format(activity_fee,moneyf))
    if inout == 2:
        print('Capital Fee                      $ ' + format(capital_fee,moneyf))
    print('Total Cost                       $ ' + format(total,moneyf))
    print('Scholarship Amount               $ ' + format(scholarshipamt,moneyf))
    print('Balance                          $ ' + format(balance,moneyf))
    print(line)
    print(str(datetime.datetime.now()))
main()