"""
Tuples are the lists which we cannot change once they have  
constructed.

Tuples are immutable.
Immutable: things which cannot be change.
Mutables:  things which can be change.

Tuple or ()

=====================================
Typecast between a list and a tuple:

A=(1,2,3,4,5,6)
B=list(A)
NOW,
B=[1,2,3,4,5,6]
C=Tuple(B)
now,
C=(1,2,3,4,5,6)

"""

A = ("Apple", "Banana", "Orange")
B = A[::-1]
print(type(B))
