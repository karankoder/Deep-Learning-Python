dict={"kolkata":100,"bombay":50,"delhi":100,"madras":400}    #donot store duplicate element
print(dict)     #dictionaries are ordered means print in the same order as it is
print(len(dict))
print(dict["delhi"])      #throw an error if key is not present
print(dict.get("delh"))   #print "None" if not present

print((dict.keys()))        #for accessing all the keys

print(dict.values())      #for accessing all the values

for i in dict:
    print(i)       # print all the key only

for i in dict:
    print(i,dict[i])

print(dict.items())

for i in dict.items():
    print(i)            #print in tuples format
for i,j in dict.items():
    print(i,j)