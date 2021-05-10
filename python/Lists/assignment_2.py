"""
Write a function called showNumber that takes the parameter called limit.
it should print all number between 0 and limit with a lable to identify the even
number and odd numbers. For example , if the limit is 3, it should print:

* 0 EVEN
* 1 ODD
* 2 EVEN
* 3 ODD

"""
print("Please entre the limit")
limit = int(input())


def shownumber():
    for i in range(0, limit+1):
        if(i % 2 == 0):
            print(i, "EVEN")
        else:
            print(i, "ODD")


shownumber()
