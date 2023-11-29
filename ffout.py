# Name: Jacob Keating
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
net_pay = []
ret_pay = []


total_net = 0
total_gross = 0

pay_rate = (16.50, 15.75, 15.75, 19.50)

DED_RATE = (.12, .03, .062, .0145, .04)

def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):

        if job[i] == "C":
            pay = hours[i] * pay_rate[0]
        elif job[i] == "S":
            pay = hours[i] * pay_rate[1]
        elif job[i] == "J":
            pay = hours[i] * pay_rate[2]
        else:
            pay = hours[i] * pay_rate[3]

        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        social = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]

        net = pay - fed - state - social - med - ret

        total_gross += pay
        total_net += net
        print(pay)

        gross_pay.append(pay)
        fed_tax.append(fed)
        net_pay.append(total_net)
        state_tax.append(state)
        soc_sec.append(social)
        medicare.append(med)
        ret_pay.append(ret)


def create_output_file():
    currency = '<10,.2f'
    line = '\n-------------------------------------------------'
    tab = '\t'
    out_file = "./payroll.txt"
    f = open(out_file, "w")

    f.write(line)
    f.write('\n************** FRESH FOODS MARKET ***************')
    f.write('\n------------- WEEKLY PAYROLL REPORT -------------')
    f.write(tab + str(datetime.datetime.now()))
    f.write(line)
    titles = "\nEmp Name" + 2*tab + "Code" + tab + "Gross" + 2*tab + "Fed Inc Tax" + 2*tab + "State Inc Tax" + 2*tab + "Soc Sec" + 2*tab + "Medicare" + tab + "Retirement" + 2*tab + "Net"
    f.write(titles)
    for i in range(num_emps):
        data = "\n" + emp[i] + tab + job[i] + tab + format(gross_pay[i], currency) + tab + format(fed_tax[i], currency) + 2*tab + format(state_tax[i], currency) + 3*tab + format(soc_sec[i], currency) + tab + format(medicare[i], currency) + tab + format(medicare[i], currency)+ 2*tab  + format(net_pay[i], currency)
        f.write(data)
    f.write(line)
    f.write("\n********************* TOTAL GROSS: $" + format(total_gross, currency))
    f.write("\n********************* TOTAL NET  : $" + format(total_net, currency))
    f.write(line)
    f.close()
    print("Open " + out_file + " to view your report")

main()