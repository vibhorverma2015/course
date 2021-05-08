"""
create a programm in which the user gives the input
and same number pf * can be printed in each row

n=5
*
**
***
****
*****
n=3
*
**
***
"""

print("please entre the number_of rows", end=" ")
number_of_rows = int(input())
for rows in range(1, number_of_rows + 1):
    for numberofstars in range(rows):
        print("*", end=" ")
    print()
