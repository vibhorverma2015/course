"""
Functions are some constructs available in programming 
language by which we can reduce duplicacy in code
and make our code easy to understand.

def <name_of_a_function>():

once a function is created you can call
its code by
<name_of_function>()

"""


# def greet():
#   print("hello everyone")
#  print("nice to meet you")

def greet():
    print("hello", user_name)
    print("nice to meet you")


print("my name is vibhor verma")

print("please entre your user_name")
user_name = input()

greet()  # calling a function
