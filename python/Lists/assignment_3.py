"""
Write a function that returns the sum of multiplies of 3 and between 0 and limit
(parameters, For example, if limit is 20, it should return the sum of 
3,5,6,9,10,15,18,20

"""
print("please entre the number")
limit = int(input())

for i in range(0, limit+1):
    if(i % 3 == 0 or i % 5 == 0):
        print(i)
