s=input("Enter the string: ")
dict={}
lst=list(s)
for i in lst:
    dict[i]=lst.count(i)
# print(dict)
for i,j in dict.items():
    print(i,j)