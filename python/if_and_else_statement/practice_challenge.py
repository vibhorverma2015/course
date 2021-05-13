"""
If a number is divisible by 3 print FIZZ
If a number is divisible by 5 print FUZZ
If a number is divisible by both print FIZZ_BUZZ

"""
user_input = float(input())

if (user_input % 5 == 0 and user_input % 3 == 0):
    print("FIZZ_FUZZ")
else:
    if (user_input % 5 == 0):
        print("FUZZ")
    if (user_input % 3 == 0):
        print("FIZZ")
