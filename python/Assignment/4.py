s=input("Enter the string: ")
lst=list(s)
lst.sort()
str=""
for i in lst:
    str=str+i
print(str)