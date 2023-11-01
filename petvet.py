# NAME : Jacob Keating
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia
#
# PET CARE MEDS Pricing
#------------------------------
# Canine Vaccines:
#   1. Bordatella $30.00
#   2. DAPP $35.00
#   3. Influenza $48.00
#   4. Leptospirosis $21.00
#   5. Lyme Disease $41.00
#   6. Rabies $25.00
#   7. Full Vaccine Package (includes all vaccines): 15% discount
# 
# Canine Heartworm Preventative Chews (prise per chew: one chew per month)
#   Small dogs, Up to 25 lbs: $0.99
#   Medium-sized dogs, 26 to 50 lbs: $11.99
#   Large dogs: 51 to 100 lbs: $13.99

import datetime

######## define global variables #########
# define dog prices
dog_vax_arr = ["Bortadella", "DAPP", "Influenza", "Leptospirosis", "Influenza", "Lyme Desease", "Rabies", "Full Vaccine Package", "NONE"]
cat_vax_arr = ["Leukemia", "Viral Rhinotracheitis", "Rabies", "Full Vaccine Package"]


PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEP = 21
PR_LYM = 41
PR_RAB = 25
PR_DLL = 0
PR_LEU = 35
PR_RHI = 30
PR_CLL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99
PR_CHEWS_CAT = 8.00

# define global variables
########## define program functions #########
def main():
    more = True

    while more:
        get_user_data()
        
        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like to process another pet (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO": 
            more = False
            print('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input('Pet name: ')
    pet_type = input('Is this a pet dog (D) or cat (C)? ')
    pet_weight = int(input('Weight of your pet (in pounds): '))

############### DOG FUNCTIONS ##############

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n** Dog Vaccines: \n\t1.Bortadella \n\t2.DAPP \n\t3.Influenza \n\t4.Leptospirosis"
    dog2 = "\n\t5.Influenza \n\t6.Lyme Desease  \n\t7.Rabies \n\t8.Full Vaccine Package \n\t9.NONE"
    dogmenu = dog1 + dog2
    pet_vax_type = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all dogs.\n")

    heart_yesno = input("Would you like order monthly heart worm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))
    else: num_chews = 0

def perform_dog_calculations():
    global vax_cost, chews_cost, total

    # vaccines

    if pet_vax_type == 1:
        vax_cost = PR_BORD

    elif pet_vax_type == 2:
        vax_cost = PR_DAPP

    elif pet_vax_type == 3:
        vax_cost = PR_FLU

    elif pet_vax_type == 4:
        vax_cost = PR_LEP

    elif pet_vax_type == 5:
        vax_cost = PR_LYM

    elif pet_vax_type == 6:
        vax_cost = PR_RAB

    else:
        PR_ALL = PR_BORD+PR_BORD+PR_DAPP+PR_FLU+PR_LEP+PR_LYM+PR_RAB
        vax_cost = .85 * PR_ALL
    
    # heart chew cost
    chews_cost=0
    if num_chews != 0 :
        if pet_weight <= 25:
            chews_cost = num_chews * PR_CHEWS_SMALL
        elif pet_weight > 25 and pet_weight < 50:
            chews_cost = num_chews * PR_CHEWS_MED
        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    #find total
    total = vax_cost + chews_cost

def display_dog_results():
    line ='-----------------------------------------'
    moneyf = '>10,.2f'
    print(line)
    print('****** PET VACCINES AND MEDICATION ******')
    print(line)
    print('Vaccine Received: ' + "{:>23}".format(dog_vax_arr[pet_vax_type-1]))
    print('Vaccine Cost                 $ ' + format(vax_cost,moneyf))
    if num_chews > 0:
        print('Heartworm Chew Cost          $ ' + format(chews_cost,moneyf))
    print('Total Cost                   $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))

############### CAT FUNCTIONS ##############

def get_cat_data():
    global pet_vax_type, num_chews
    catmenu = "\n** Cat Vaccines: \n\t1.Feline Leukemia \n\t2.Feline Viral Rhinotracheitis \n\t3.Rabies (one year) \n\t4.Full Vaccine Package"
    pet_vax_type = int(input(catmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heart worm prevention medication is recommended for all cats.\n")

    heart_yesno = input("Would you like order monthly heart worm medication for " + pet_name + " (Y/N)? ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heart worm chews would you like to order? "))
    else: num_chews = 0

def perform_cat_calculations():
    global vax_cost, chews_cost, total
    if pet_vax_type == 1:
        vax_cost = PR_LEU

    elif pet_vax_type == 2:
        vax_cost = PR_RHI

    elif pet_vax_type == 3:
        vax_cost = PR_RAB

    else:
        PR_ALL = PR_LEU+PR_RHI+PR_RAB
        vax_cost = .85 * PR_ALL

    if num_chews != 0:
        chews_cost = num_chews * PR_CHEWS_CAT
    else: chews_cost = 0

    total = vax_cost + chews_cost

def display_cat_results():
    line ='-----------------------------------------'
    moneyf = '>10,.2f'
    print(line)
    print('****** PET VACCINES AND MEDICATION ******')
    print(line)
    print('Vaccine Received: ' + "{:>23}".format(cat_vax_arr[pet_vax_type-1]))
    print('Vaccine Cost                 $ ' + format(vax_cost,moneyf))
    if num_chews > 0:
        print('Heartworm Chew Cost          $ ' + format(chews_cost,moneyf))
    print('Total Cost                   $ ' + format(total,moneyf))
    print(line)
    print(str(datetime.datetime.now()))
    

main()