"""
Program to check is the year 
provided by the user is the leap year or not.

"""


print("Hello!")
print("Please mention the year below")
Year = int(input())
if(Year % 4 == 0):
    print(Year, "It is a leap year :)")
else:
    print(Year, "It is not a leap year :(")
