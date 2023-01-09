mylist =['albin','anandhu','aswin','akash']
print(mylist)
str = ""
for i in mylist:
    str = str + i

count = 0
for i in range(len(str)):
    if str[i] == "a":
        count = count+1
print("count of a :",count)