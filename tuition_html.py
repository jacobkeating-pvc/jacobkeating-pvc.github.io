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
outfile = "tuition.html"


######## define program functions ########
def main():

    open_outfile()
    more_tickets = True
    
    while more_tickets:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        askAgain = input("\nWould you like to calculate tuition & fees for another student? (Y or N)?: ")
        if askAgain.upper() == 'N':
            more_tickets = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<link rel="stylesheet" href="tuition.css">\n')
    f.write('<html> <head> <title>PIEDMONT VIRGINIA COMMUNITY COLLEGE</title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body>\n')

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

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "2" style="text-align: center;">'
    sp = " "

    f.write('\n<table>\n')            
    f.write(colsp + '\n')
    f.write('<h2>PIEDMONT VIRGINIA COMMUNITY COLLEGE</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** PVCC college tuition & fees ***\n')

    if inout == 1:   
        f.write(tr + 'In/Out Tuition' +  endtd + sp + 'IN STATE' + endtr)
        f.write(tr + 'Tuition Amount' + endtd + sp + format(ituition, currency) + endtr)
    elif inout == 2:
        f.write(tr + 'In/Out Tuition' +  endtd + sp + 'OUT OF STATE' + endtr)
        f.write(tr + 'Tuition Amount' + endtd + sp + format(otuition, currency) + endtr)
        f.write(tr + 'Capital Fee' + endtd + sp + format(capital_fee, currency) + endtr)

    f.write(tr + 'Total Cost' +  endtd + sp + format(total,currency)  + endtr)     
    f.write(tr + 'Scholarship Amount ' + endtd + sp + format(scholarshipamt,currency) + endtr)
    f.write(tr + 'Balance' +     endtd + sp + format(balance ,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')


main()