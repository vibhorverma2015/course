A = [1, 2, 2, 2, 4, 5, 6, 6, 7]
target = 3


def getlowerbound(A, target):
    prev = 1
    for i in range(0, len(A)):
        if A[i] == target:
            return i
        elif A[i] > target:
            return prev
        prev = i


if __name__ == "__main__":
    print(getlowerbound(A, target))
