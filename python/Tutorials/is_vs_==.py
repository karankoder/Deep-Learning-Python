# is compare the exact location in memory   # it returrns false while comparing same immutable object
# == compare the values

p=8
q=8    #both have same locaion as it is immutable
print(p is q)
print(p==q,end="\n\n")

a=[1,2,3]
b=[1,2,3]
# a[0]=100
print(a)
print(a is b)
print(a==b)