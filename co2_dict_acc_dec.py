y = {'alen': 40, 'albin': 12, 'job': 45, 'teena': 13}

l = list(y.items())
print('Ascending :', l)
l.sort(reverse=True)
print('Descending :', l)
dict = dict(l)

print("Dictionary", dict)