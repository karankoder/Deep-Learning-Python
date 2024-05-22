s1={1,2,5,8,10}
s2={5,8,10,20}
print(s1.union(s2))   # this will not affect the value of set s1 and s2

#if we want to update the value of s1 then
s1.update(s2)
print(s1)

print(s1.intersection(s2))

s1.intersection_update(s2)      # update the value of the set s1
print(s1)

#symmetric difference - union minus intersection
c1={"kolkata","chennai","delhi","bombay"}
c2={"madras","delhi","roorkee","BHU"}
print(c1.symmetric_difference(c2))

print(c1.difference(c2))    #c1-c2
#important if we want to update the value then we use _update

#disjoint-no intersection element
print(c1.isdisjoint(c2))

print(c1.issuperset(s2))

print(c1.issubset(c2))

c1.add("rio")
print(c1)

c1.remove("kolkata")        #it will raise an error if element is not present
print(c1)       

c1.discard("rio")           #it will not raise an error
print(c1)

print(c1.pop())             #pop any random element
print(c1)

c1.clear()                  #clears all element in set
print(c1)

del c1                      #for deleting the whole set