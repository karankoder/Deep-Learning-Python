a=int(input("Enter your age: "))
if(a>=18):
    print("Eligible")
else:
    print("Baby")        #always leave the intendation

#match case

match(a):
    case 5:
        print("Noob")
    case 18:
        print("Pro")
    case _:                   #default
        print("Null")

    
