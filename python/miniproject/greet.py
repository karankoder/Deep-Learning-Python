import time as t

name=input("Enter your name: ")
time=int(t.strftime("%H",t.localtime()))
day=t.strftime("%A",t.localtime())
date=t.strftime("%d/%m/%y",t.localtime())
ti=t.strftime("%H:%M:%S",t.localtime())
t.sleep(1)
if(time>=5 and time<12):
    print(f"Good Morning {name}")
    t.sleep(1)
elif(time>=12 and time<17):
    print(f"Good Afternoon {name}")
    t.sleep(1)
elif(time>=17 and time<22):
    print(f"Good Evening {name}")
    t.sleep(1)
else:
    print(f"Good Night {name}")
    t.sleep(1)
print(f"Today is {day}")
t.sleep(1)
print(f"Time : {ti}")
t.sleep(1)
print(f"Date : {date}")




