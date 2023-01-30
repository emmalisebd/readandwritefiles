import csv

infile = open("sales.csv", "r")
outfile = open("salesreport.csv", "w")

csvreader = csv.reader(infile, delimiter=",")

outfile.write("Customer | Total \n")
for detail in csvreader:
    custID = detail[0]
    total = float(detail[3]) + float(detail[4]) + float(detail[5])
    new_record = "custID" + " " + "total" 

infile.close() 
outfile.close()
