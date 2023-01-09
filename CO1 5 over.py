newlist = []
n = int(input("Enter the size of list:"))
for i in range(n):
    item = int(input("Enter Element :"))
    newlist.append(item)
print(newlist)

for i in range(n):
    if newlist[i] > 100:
       newlist[i] = "OVER"
print(newlist)
