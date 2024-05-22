#Lists are mutable datatype
#list can store multiple datatypes
marks=[1,6,55,55,5,"python","Time"]
print(marks)
marks[0]=50
print(marks)
for i in marks:
    print(i)
if 55 in marks:
    print("Yes its present in list")

#List slicing
print(marks[1:5:2])

list=[i*i for i in range(10) if(i%2==0)]
print(list)
print(len(marks))

lst=[5,8,87,8,75,7,287]
lst.append(100)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst.reverse()
print(lst)

print(lst.index(100))      #index of first occurence

print(lst.count(100))

m=lst  # m is a reference variable means if we change the value in lst then it also change the value of m
lst[0]=45454
print(m)
print(lst)

m=lst.copy()
lst[0]=50000000
print(m)
print(lst)

lst.insert(1,52)     #index number and then value
print(lst)

lst.extend(marks)
print(lst)

k=lst+marks
print(k)

k.pop()       #removes last element
print(k)

k.pop(4)        #remove the element at 4th index
print(k)     

po=[1,2,3,5,5,5]
qo=[878,98,87,87,877,87,88]
qo.pop(1)
qo.remove(87)
print(qo)





