"""
Parameterized_function is a function which take inputs also
which are called parameters to the function

The parameters are the types of python only
eg., int , str, float, list etc

and a function can return some data which also are of types
eg., int, str,float,list,etc

to get the output from the function we use the keyword
   return

"""

a = int(input())
b = int(input())


def add_two_number(a, b):
    return(a+b)
    print(ans)


def multiply_two_number(a, b):
    return(a*b)
    print(ans)


ans = add_two_number(a, b)
print(ans)

ans = multiply_two_number(a, b)
print(ans)
