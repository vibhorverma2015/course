"""
user will give you n youn have to print
table til n * 10 =

user_input =4
table of 4 is:

table of 4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
......

4 * 10 = 40

"""

for i in range(1, 21):
    print("****************")
    print("Table of", i)
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
    print("****************")
