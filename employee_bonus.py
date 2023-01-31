import csv

infile = open("EmployeePay.csv", "r")
csvreader = csv.reader(infile, delimiter=",")
next(csvreader)

for detail in csvreader:
    print(
        format(detail[0]),
        format(detail[1]),
        format(detail[2]),
        format(detail[3]),
        format(detail[4]),
        format(float(detail[3]) + float(detail[3]) * float(detail[4])),
        input(),
    )

infile.close()
