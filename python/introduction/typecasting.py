"""
when we have to change the variable or data from one nature / form to another 
form/ nature then "typecasting" is used.


we use typecasting to change String , Integer & flout

>>> a = "5" {it is in the string forn}
to convert it in the integer form we can write the code

a = int(a) {then the a converts from string to integer}


"""

print("typecasting from string to integer")

a = "5"
print("before", type(a))

a = int(a)
print("after", type(a))


print("typecasting from integer to float")
a = 5
print("before", type(a))

a = float(5.7)
print("after", type(a))
