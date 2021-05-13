"""
Scopes:
=============================
example :1
def ABC():
    sum = 10
    for x in range(10):
        sum = 0
    print(sum)

ABC()
=============================

Example: 2
sum = 0 # global scope
def ABC():
    sum = 5 # local scope
    print("inner sum", sum)

ABC()

print("outer sum", sum)

Global scope: any variable outside a function is called to be in global
              scope

Local scope: any variable inside a function is called to be
              a local scope
 ======================================================
 Example:3

 sum = 0


def ABC():
    sum = 5
    for i in range(1, 10):
        sum += 5
        print("inner sum", sum)


ABC()

print("outer sum", sum)
================================================

"""

sum = 0


def ABC():
    sum = 5
    for i in range(1, 10):
        sum += 5
        print("inner sum", sum)


ABC()

print("outer sum", sum)
