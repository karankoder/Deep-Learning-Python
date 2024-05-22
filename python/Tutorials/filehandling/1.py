f=open("abcd.py",'r')   # r mode is default
print(f)

text=f.read()
print(text)
f.close()

f=open("a.txt",'w')
f.write("Hello World i am writing some new contein in this file")
f.close()

f=open("a.txt",'a')
f.write("now i have appended some item in the file, write mode delete all the previous content of the file and write new content.")
f.close()

f=open("a.txt",'r')
text=f.read()
print(text)
f.close()

with open("abcd.py",'a') as f:
    f.write("program ended")       # this will automatically open and close the file



