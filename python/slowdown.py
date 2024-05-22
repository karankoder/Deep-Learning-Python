import time as t

# for i in range(10):
#     t.sleep(1)
#     print(i)

print(t.gmtime(0))      
print(t.time())
print((t.ctime()))

# print((t.localtime()))
print((t.strftime("%a, %d %b %Y %H:%M:%S",t.localtime())))