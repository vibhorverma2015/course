limit = int(input())
for i in range(0, limit+1):
    if(i % 1 == 0 and i % 2 != 0):
        print(i, end=" ")
