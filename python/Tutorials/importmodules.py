# import math

# print(round((math.sqrt(10)),4))    # here we have to use full name ie math to implement any function

from math import *                  # to import all contents
print(sqrt(5)*pi)                  # if we want to use only some specific function

import math as m                    

print(round((m.sqrt(10)),4))         # for short form notation
print(dir(m))                         # give all the functions available

import karan
karan.welcome()             # to avoid printing welcome karan we use __name__
print(karan.k)
