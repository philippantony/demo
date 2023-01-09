import csv

column_to_read = [0,2]

with open("new1.csv","r") as f:
    clmn_reader = csv.reader(f)

    for row in clmn_reader:
        print([row[i] for i in column_to_read])