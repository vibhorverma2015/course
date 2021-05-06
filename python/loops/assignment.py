"""
make a calculator which do addition/substraction/multiplication/division 
and show the table of the number

"""


print("Hello! my name is calculator")
first_num = float(input())
print("choose one command")
print("+, for addition")
print("-, for substraction")
print("*, for multiplication")
print("/, for division")
command = input()
second_num = float(input())

if(command == "+"):
    print(first_num, "+", second_num, "=", first_num+second_num)
elif(command == "-"):
    print(first_num, "-", second_num, "=", first_num-second_num)
elif(command == "*"):
    print(first_num, "*", second_num, "=", first_num*second_num)
elif(command == "/"):
    print(first_num, "/", second_num, "=", first_num/second_num)
else:
    print("error!")
