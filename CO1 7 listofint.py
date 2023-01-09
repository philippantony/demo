list1= [11,2,6,4]
list2= [10,2,5,4]
if len(list1) == len(list2):
    print("list are of same length")
else:
    print("list are not of same length")
sum1 = 0
sum2 = 0

for i in list1:
    sum1 = sum1 + i
for i in list2:
    sum2 = sum2 + i

print(sum1)
print(sum2)
if sum1 == sum2:
    print("Sum of two list are SAME")
else:
    print("Sum of two list are NOT SAME")

s1 = set(list1)
s2 = set(list2)

print("Common Elements is:",s1.intersection(s2))