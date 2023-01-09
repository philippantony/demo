
s = int(input("Enter current year :"))
e = int(input("Enter final year"))

for year in range(s, e):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year)