square= lambda x: x*x
cube= lambda x : x*x*x
average= lambda x,y: (x+y)/2
modl= lambda x: x if (x>=0) else -x

print((lambda x: x*x)(100))
print(cube(5))
print(average(5,8))
print(modl(-5))
