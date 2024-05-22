a=input("Enter the binary number: ")
print("Decimal of",a,"=",int(a,2))


b=int(input("Enter the decimal number: "))
print("Binary of",b,"=",bin(b).replace("0b",""))
print("Binary of",b,"=",bin(b)[2:])
print(bin(b))