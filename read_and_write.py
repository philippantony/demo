# open file in read mode
input_file = open("Data.txt")

# open file in write mode
output_file = open("WriteData.txt", "w")

# display data
copydata = input_file.readlines()
print("---Actual Data---")
print(copydata, "\n")

# display the data
for i in range(0, len(copydata)):
    if i % 2 == 0:
        output_file.write(copydata[i])
    else:
        pass

# closing the outputfile
output_file.close()


# opening the written file
output_file = open("WriteData.txt", "r")
print("---Odd lines are---")
print(output_file.read())

# closing
input_file.close()
output_file.close()
