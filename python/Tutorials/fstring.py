letter="Hello my name is {} and i am from {}"
print(letter.format("karan","kolkata"))           #in this case we have to give our value in order

name="karan"
place="kolkata"

print(f"Hello my name is {name} and i am from {place}")
price=545454
tx="I will give you {} dollars!"
print(tx.format(price+1))
p=58.099999999
txt=f"I will give you {p:.4f} dollars!"     # round off
print(txt)

a=7
q=str(7)
print(type(q))
print(f"{2**3}")