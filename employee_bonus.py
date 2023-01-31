import csv

infile = open("EmployeePay.csv", "r")
csvreader = csv.reader(infile, delimiter=",")

for detail in csvreader:
    print(
        format(detail[0]),
        format(detail[1]),
        format(detail[2]),
        format(detail[3]),
        format(detail[4]),
    )

infile.close()
