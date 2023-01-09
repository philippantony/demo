text = str(input("Enter your text :"))
list = text.split(" ")

for j in list:
    c = 0
    for i in list:
        if i == j:
            c = c+1
    print("Occurrences of",j,"=",c)