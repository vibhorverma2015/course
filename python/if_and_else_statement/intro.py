"""
In this section we will learn about if / else statement

>>> if(<boolean_condition>):
     print("hi")
     a=3
     b=4
     print(a+b)


"""

a=10
if(a % 2 == 0 or a > 20):
    print("the number is even")

print("this program is completed")

a=8
if(a % 2 == 0 or a>=8):
    if(a % 2==0):
        print("the number is even")
    if(a >= 8):
        print("the number is 8")
        if(a <= 10):
            print("the number is less than 10")

print("programme completed")
