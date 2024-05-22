import random
lst=[]

for i in range(100):
    lst.append(random.randint(1000000000,9999999999))

result=[]
result.append(random.choice(lst))
result.append(random.choice(lst))
print(result)
