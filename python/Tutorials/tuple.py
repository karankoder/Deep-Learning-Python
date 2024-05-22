#tuples are almost similar to the list
#Only difference-
#list - mutable
#tuple - immutable
#we cant add change or remove elements in tuples
t=(1,8,4,8,4,4)
print(t)
#to make any changes at first we have to make tuples into list

temp=list(t)
print(temp)

temp.append("Hello")
temp1=tuple(temp)
print(temp1)

#for finding element in tuple
print(temp1.index(4,1,5))        # value, starting index, ending index

tuple1=(1,)
print(type(tuple1))

tuple2=()
print(type(tuple2))
