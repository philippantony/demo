mylist = [1,2,3,4,5,6,7,8,9,10,11]
print(mylist)
for i in mylist:
    if i % 2 == 0:
        mylist.remove(i)
print(mylist)
