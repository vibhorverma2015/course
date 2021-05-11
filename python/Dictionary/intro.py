"""
Dictionary:
A dictionary is a data structure which has key and value.

Dictionary is represented by a curly brackets i.e., {} or dict

Dictionary & map are the same things.

Dictionary has the property of key and value
e.g.,  {
    key1:value1,
    key2:value2,
    key3:value3,
}

key can only be (str or int or float) and value can be any data type 
eg(str,int.list,float,tuple)

"""
state_capital_dict = {
    "Delhi": "Delhi",
    "Punjab": "Chandigarh",
    "MP": " Bhopal",
}
print(state_capital_dict)


# Q. given a list with values [1,2,1,1,1,2,3,4,5,5]
# Tell the frequency of each value eg 1->4, 2->2, 3->1, 4->1, 5->2

value = 1, 2, 1, 1, 1, 2, 3, 4, 5, 5

list_dict = {1, 2, 1, 1, 1, 2, 3, 4, 5, 5}
for value in list_dict.value():
    print("for value", value, "frequwncy is", list_dict[value])
