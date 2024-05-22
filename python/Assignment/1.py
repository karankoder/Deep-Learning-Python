t=int(input("Enter the number of testcase: "))
for i in range(t): s=(input()); print("Empty String") if(len(s)<2)  else print(s[:2],s[(len(s)-2):],sep="")