import csv

with open("new1.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)