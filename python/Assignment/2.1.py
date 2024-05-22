x = {'key1': 1, 'key2': 1, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for key,value in x.items() & y.items():
  print("{}: {} is present in both x and y".format(key,value))