# NAME: Joshua Vernon 
# NAME: Jacob Keating
# Prog purpose: This program finds the cost of adults and children at a restaurant
#   Price for one adult: $19.95
#   Price for one child: $11.95
#   Sales tax rate: 6.2%
#   Service fee rate: 10%

import datetime

########## define global variables ##########
# define tax rate and prices

SALES_TAX_RATE = 0.055
PR_TICKET = 10.99

# define global variables

num_tickets = 0 
subtotal = 0
sales_tax = 0
total = 0


##### define program functions #####

def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False
            print("Thank you for your order. Enjoy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax


def display_results():
    line = '--------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** CINEMA HOUSE MOVIES ****')
    print('Your neighborhood movie house')
    print(line)
    print('Tickets            $ ' + format(subtotal,moneyf))
    print('Sales Tax           $ ' + format(sales_tax,moneyf))
    print('Total               $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

###### call on main program to execute ########
main()












