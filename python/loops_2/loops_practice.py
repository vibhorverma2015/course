"""
given n print the sum of cubes of all the number fromm
1 to n
"""
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i ** 3
print(sum)
