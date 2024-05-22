a=4
b=10

def swap():
    global a
    global b
    temp=a
    a=b
    b=temp
print(f"Before swapping a= {a} and b ={b}")
swap()
print(f"After swapping a= {a} and b = {b}")




