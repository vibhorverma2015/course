"""
elif is the term where we check every situation one by one 
if the if condition is not true. 

then elif can check every situation one by one if any
one of them is correct then it will  execute that elif otherwise 
if not  a single situation is correct pr true
then it will execute the only else situation at the last.


"""

weather = "snowy"

if(weather == "raining"):
    print("i will use the rain coat")
elif(weather == "stormy"):
    print("i will use the car")
elif(weather == "snowy"):
    print("i will stay at home")
elif(weather == "sunday"):
    print("i will do party")        
else:
    print("i will sleep")