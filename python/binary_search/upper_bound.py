a = [1, 2, 2, 3, 3, 3, 5, 7, 8, 8, 8, 10]
target = 9


def get_upperbound(a, target):
    prev = 1
    for i in range(0, len(a)):
        if a[i] == target:
            return i
        elif a[i] > target:
            return prev+1
        prev = i


if __name__ == "__main__":
    print(get_upperbound(a, target))
