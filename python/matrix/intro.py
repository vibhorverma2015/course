A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(A)  # length of row
m = len(A[0])  # length of columns

x = 3

# for i in range(m):
#    print(A[x-1][i])

#c = 1
# for i in range(n):
#   print(A[i][c-1])

# for i in range(n):
#   for j in range(m):
#      print(A[i][j], end=" ")
# print()

r = 0
c = 0

while r < n and c < m:
    print(A[r][c])
    r += 1
    c += 1


B = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3]

]

n = len(A)
m = len(A[0])

for i in range(min(m, n)):
    print(B[i][i])
