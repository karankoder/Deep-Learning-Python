with open("a.txt",'r') as f:
    print(type(f))
    f.seek(5)         # readthe content after 5 bytes (1 based indexing followed)
    text=f.read(10)   #read only first 10 bytes
    print(text)

    print(f.tell())   #tells the current position

with open("a.txt",'w') as f:
    f.write("Now i am using truncate keyword")
    f.truncate(10)      #this means we want only 10 characters in the file
