# program to read file using readlines

# opening a file
file = open('newfile.txt', 'r')

# reading using realines method
file_lines = file.readlines()


print("----File Content----")
print(file_lines)  # printing the list


print("\n ----File Content after using Strip Function----")
file_lines = [x.strip() for x in file_lines]
print(file_lines)
file.close()
