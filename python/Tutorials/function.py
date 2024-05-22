def prime_number(n=100):
    p=0
    for i in range(2,n):
        if(n%i==0):
            p=p+1
    if(p==0):
        return True
    else:
        return False
a=int(input("Enter the number to check: "))
if(prime_number(a)):
    print("It's a prime number")
else:
    print("It's not prime.")


