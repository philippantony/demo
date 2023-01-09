str = input("Enter a String :")
if str[-1] == 'g' and str[-2]=='n' and str[-3] == 'i':
  str += 'ly'
else:
  str += 'ing'

print(str)