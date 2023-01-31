import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

csvreader = csv.reader(infile, delimiter=",")
next(csvreader)

outfile.write("Customer ID | Total \n")

custID = "250"
cust_total = 0

for detail in csvreader:
    if custID != detail[0]:
        print(cust_total)
        outfile.write((str(custID)) + "\t\t\t\t" + str("%.2f" % cust_total) + "\n")
        custID = detail[0]
        cust_total = 0

    total = float(detail[3]) + float(detail[4]) + float(detail[5])
    cust_total += total

outfile.write(("261") + "\t\t\t\t" + str("%.2f" % cust_total) + "\n")


infile.close()
outfile.close()
