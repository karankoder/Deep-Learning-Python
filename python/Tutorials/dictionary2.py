e1={125:54,123:89,125:45,685:55}
e2={1:100,565:87}
print(e1,e2)
e1.update(e2)
print(e1)

e2.clear()
print(e2)
empty={}     #empty dictionary


print(e1.pop(1))     #returns its value of key
print(e1)
  
e1.popitem()             #for removing the last element
print(e1)

e1[1200]=1
print(e1)