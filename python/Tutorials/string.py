#string is immutable means non changeable
a=input("Enter your first name-")
b=input("Enter your last name-")
print("Your full name is-",a+" "+b)                 #concatenation
print(len(a))

#string slicing
d="abcdefgh"
print(d[1:5])       # print from 1 to 5-1=4
print(d[-5:-1])     #total lenght - 1,   this is similar to len(d)-5 to len(d)-1
 

# x="laean\\\"    this will throw an error

#if we use r then \n wont work
print(r"sdhsjhdjh\nwjdihai")