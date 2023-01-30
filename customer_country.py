import csv

infile = open("customers.csv", "r")
outfile = open("customer_country.csv", "w")

csvreader = csv.reader(infile, delimiter=",")

next(csvreader)

outfile.write("Customer Name, Country \n")
for detail in csvreader:
    firstname = detail[1]
    lastname = detail[2]
    country = detail[4]
    new_record = firstname + " " + lastname + "," + " " + country
    outfile.write(new_record + "\n")

infile.close()
outfile.close()
