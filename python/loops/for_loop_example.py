"""
Loops are constructed in programming language 
which helps to repeat some sections 
of the codes

types of loops:
1. while loop
2. for loop

For loop

fir i in ranger(5):
    print(i)


Question: print all the no in range 0-100 if any of them 
is divisible by 3 print FIZZ
if divisible by both FIZZ-FUZZ
if any of them divisible by 5 FUZZ
else: print normal
 

"""


user_input =int(input())

for i in range(user_input +1):
    if(i % 5 == 0 and i % 3 == 0):
        print(i , "FIZZ_FUZZ")
    elif(i % 5 == 0):
        print(i, "FUZZ")
    elif(i % 3 == 0):
        print(i, "FIZZ")
    else:
        print(i)

