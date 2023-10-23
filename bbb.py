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
SALES_TAX_RATE = 0.062
SERVICE_FEE_RATE = .10
P_ADULTS = 19.95
P_CHILDREN = 11.95

# define global variables
num_adults = 0
num_children = 0
asubtotal = 0
csubtotal = 0
sales_tax = 0
service_fee = 0
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
            print("Thank you for your order!")

def get_user_data():
    global num_adults, num_children
    num_adults = int(input("Number of adults: "))
    num_children = int(input("Number of children: "))

def perform_calculations():
    global asubtotal, csubtotal, sales_tax, service_fee, total, subtotal
    asubtotal = num_adults * P_ADULTS
    csubtotal = num_children * P_CHILDREN
    subtotal = asubtotal + csubtotal
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

def display_results():
    line = '--------------------------------'
    moneyf = '8,.2f'
    print(line)
    print('**** Branch Barbecue Buffet ****')
    print(line)
    print('Number of Adults    : ' + str(num_adults))
    print('Number of Children  : ' + str(num_children))
    print(line)
    print('Adults              $ ' + format(asubtotal,moneyf))
    print('Children            $ ' + format(csubtotal,moneyf))
    print('Subtotal            $ ' + format(subtotal,moneyf))
    print('Service Fee         $ ' + format(service_fee,moneyf))
    print('Sales Tax           $ ' + format(sales_tax,moneyf))
    print('Total               $ ' + format(total,moneyf))
    print(str(datetime.datetime.now()))

###### call on main program to execute ########
main()



