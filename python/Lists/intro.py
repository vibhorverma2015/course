"""
whenever we declare  or store something in a variable the variable is assigned
to a unique address in  the RAM and the variable is stored 
at that position.

List: list is a type of data structure where all the values are present next
to each other and it has indexes which starts from 0 and go to the
(size of the list-1)

In python we denote list with
[] or list()

>>> fruits=["Apple", "Banana", "Papaya"]
>>> fruits
['Apple', 'Banana', 'Papaya']
>>> type(fruits)
<class 'list'>
>>>

api = (application programming interface or tools)

1.) To get the size of the list

len:
len(fruits): It will tell the size of the list

2.) Accessing the item of the list

fruits[1] -> Banana
fruits[2] -> Papaya
fruits[3] -> Apple

3.) Range (0,4)


"""

fruits = ["Apple", "Banana", "Papaya", "melon", "pear", "orange"]
print("length of the list", len(fruits))
print("item of the list", fruits[1], fruits[2], fruits[0])

print(fruits[0: len(fruits):2])
