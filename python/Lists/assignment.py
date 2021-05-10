"""
Write the function for checking the speed of drivers. This function should 
have one parameter:speeed
* If speed is less then 70, it should print"OK".
* Otherwise, for every 5 km above the speed limit (70), it should give
  the driver one demerit point and print the total number of demerit points.
  for example, if the speed is 80, it should print
  "points: 2".
* If the driver gets more than 12 points, the function should print:
  "License suspended"
     
"""
speed = int(input())
demerit = 0

if speed < 70:
    print("OK")
else:
    diff = speed - 70
    while diff > 0:
        demerit += 1

        if demerit > 12:
            print("licence suspended")
            break

        diff -= 5

print(demerit)
