import datetime


outfile = "tuition.html"

room_rates = []

subtotal = []
sales_tax = []
occupancy_tax = []
total = []
cust = []

grand_total = 0

infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)

def main():
    read_in_guest_file()
    perform_calculations()
    open_outfile()
    create_output_file()

def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))


def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<link rel="stylesheet" href="emerald.css">\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body>')

    
def perform_calculations():
    global total_gross, total_net, grand_total

    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])

        if room_type == "SR":
            cost = num_nights * ROOM_RATES[0]
        elif room_type == "DR":
            cost = num_nights * ROOM_RATES[1]
        else:
            cost = num_nights * ROOM_RATES[2]

        sales = cost * TAX_RATES[0]
        occu = cost * TAX_RATES[1]

        tot = cost + sales + occu


        subtotal.append(cost)
        sales_tax.append(sales) 
        occupancy_tax.append(occu)
        total.append(tot)
        grand_total += tot

def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "8" style="text-align: center;">'

    f.write('\n<table>\n')            
    f.write(colsp + '\n')
    f.write('<h2>EMERALD HOTEL BEACH & RESORT</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** List of guest, info, and fees ***\n')
    
    title = tr + 'Last Name' + endtd + 'First Name' + endtd + 'Room Type' + endtd + '# Nights' + endtd + 'Subtotal' + endtd + 'Sales Tax' + endtd + 'Occ. Tax' + endtd + 'Total' + endtr
    f.write(title)

    for i in range(len(guest)):
        lastname = str(guest[i][0])
        firstname = str(guest[i][1])
        room_type = str(guest[i][2])
        num_nights = str(guest[i][3])

        data = tr + lastname + endtd + firstname + endtd + room_type + endtd + num_nights + endtd + format(subtotal[i], currency) + endtd + format(sales_tax[i], currency) + endtd + format(occupancy_tax[i], currency) + endtd + format(total[i], currency) + endtr
        f.write(data)
    f.write('<tr><td colspan= "4" style="text-align: center;">' + 'Grand Total' + '</td><td colspan= "4" style="text-align: center;">' + format(grand_total ,currency) + endtr)
    
    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

main()