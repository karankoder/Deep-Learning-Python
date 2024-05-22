
a=input("Enter the number you want : ")
print(f"Multiplication table of {a} is - ")
try:
    for i in range(10):
        print(f"{a} X {i+1} = {int(a)*(i+1)}")
except Exception as e:
    print(e)                   
    print("invalid input")

#we can also handle some specific type of error

try:
    num=int(input("Enter the number:"))
    a=[1,2]
    print(a[num])
except ValueError:
    print("Number is not an integer")
except IndexError:
    print("index error")

try:
    l=int(input("enter the index print: "))
    b=[5,5,2,5,57,87,8]
    print(b[l])
except:
    print("Error")
finally:
    print("Finally is always executed")