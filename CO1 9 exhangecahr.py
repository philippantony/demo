string = input("Enter a string: ")
x = list(string)
temp = x[0]
x[0] = x[-1]
x[-1] = temp
print("".join(x))