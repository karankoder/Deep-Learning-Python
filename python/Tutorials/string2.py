a="!!!!!Python!!!!!!!!"
print(a.upper(),"karan")
print(a.lower())
print(a)
print(len(a))
print(a,"karan")
print(a.rstrip("!"),"karan")   # by default space
print(a.lstrip("!"))
print(a.replace("Python","karan"))      #replace all the occurences
b="hello worLd nOw i am"
print(b.split(" "))      #create a list of characters
print(b.capitalize())      #capitalize the first character   and lower all the characters except first one
print(len(b))
print(len(b.center(50)))
print(b.center(100,"."))
print(b.count("el"))
print(b.endswith("wo",0,8))     #check from 0 to n-1
st="i am an honest man"
print(st.find("ho"))       # return the index of first occurence of the string, if not found it give -1
print(st.index("ho"))      # differeence is that if we use index func then if element not found then it gives error
s="54ksnk55"
print(s.isalnum())    # without spaces
print(s.isalpha())    #no numbers
print(s.islower())
print(s.isupper())
y="heelo kjfkajf\nschshk"
print(y.isprintable())      #returns true if all the charscters are printable
q="        "
print(q.isspace())
str="Kek Hsms sheuf jwhdk"
print(str.istitle())        #returns true if the first letter of all words are capital
print(str.title())
print(str.swapcase())       # upper to lower and vice versal
print("python "*5 +"Hello")
