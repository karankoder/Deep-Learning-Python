# readline is used to read the content of the file line by line
f=open("a.txt",'r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    s1=line.split(",")[0]
    s2=line.split(",")[1]
    s3=line.split(",")[2]
    print(f"Marks of student {i} in maths is {s1}")
    print(f"Marks of student {i} in english is {s2}")
    print(f"Marks of student {i} in physics is {s3}")

#writeline is used to write a sequence of strings to a file, the sequence acn be a list or tuple

f=open("a.txt",'w')
line=['line1\n','line2\n','line3\n','line4\n']
f.writelines(line)
f.close()

#this is very similar to
f=open("a.txt",'w')
for l in line:
    f.write(l+"\n")
f.close()



