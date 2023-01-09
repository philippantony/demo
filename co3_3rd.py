import random
import os
print("Select a random element from a list:")
element = [1,2,3,4,5]
print(random.choice(element))
print(random.choice(element))
print(random.choice(element))
print(" Select a random element from a set :")
element = set([1,2,3,4,5])
print(random.choice(tuple(element)))
print(random.choice(tuple(element)))
print(random.choice(tuple(element)))
print("\nSelect a random value from a dictionary:")
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
key = random.choice(list(d))
print(d[key])
print("\nSelect a random file from a directory.:")
print(random.choice(os.listdir("/")))


