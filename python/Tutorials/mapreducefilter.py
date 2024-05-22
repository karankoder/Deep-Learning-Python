from functools import reduce
lst=[5,4,85,1,2,4,10,8] 
print(list(map(lambda x:x*x,lst)))      #applies on each function
print(list(filter(lambda x: x%2==0,lst)))  #return the element which is true only

print(reduce(lambda x,y:x+y ,lst))
print("EOP")