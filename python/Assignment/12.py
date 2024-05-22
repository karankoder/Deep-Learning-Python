lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
dict={}
lst2=[]
for i in lst:
    if(lst2.count(i)==0):
        lst2.append(i)
print(lst2)
