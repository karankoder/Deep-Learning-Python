a='''Hello 
    python
    pycharm 
    turtle'''
print(a)

#Whenever string literals are present just after the function definition it's referred as docstring

def square(n):
    #print("karan")
    '''its a docstring and this function returns the square of a number'''#remember its written just after func. def
    print(n**5)
square(10)
print(square.__doc__)