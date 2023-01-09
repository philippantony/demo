n = int(input("Input an integer : "))
sum = 0
for i in range(3):
  ph = int(pow(n, i+1))
  print(ph)
  sum = sum + ph
print("SUM IS :",sum)