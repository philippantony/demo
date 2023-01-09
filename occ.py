text = str(input("Enter your text :"))
list = text.split(" ")
count = 0
set1 = set(list)
for i in set1:
    for j in range(0,len(list)):
        if i == list[j]:
            count =count+1
    print("count of ",i,"is",count)
    count = 0
