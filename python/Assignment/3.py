s=input()
a=s.find('not')
b=s.find('poor')
if(a!=-1 and b!=-1 and a<b):
    print(s.replace(s[a:b+4],"good"))