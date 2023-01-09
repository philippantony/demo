import pandas as pd

data = pd.read_csv('emp.csv')

print(data.to_string())
count = 0
count = len(list(data))
print("count is :",count)