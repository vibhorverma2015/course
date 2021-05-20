a = [1, 11, 22, 33, 44, 55, 66, 77, 88, 99,
     110, 120, 232, 343, 434, 546, 754, 856, 999]
target = 546

left = 0
right = len(a)-1


def binary_search(a, target):
    while left <= right:
        mid = (right+left)//2
        if a[mid] == target:
            return mid
        elif a[mid] >= target:
            right = a[mid]-1
        else:
            left = a[mid]+1
    return None


if __name__ == "__main__":
    a = [1, 11, 22, 33, 44, 55, 66, 77, 88,
         99, 110, 120, 232, 343, 434, 546, 754, 856, 999]
target = 546

print(binary_search(a, target))
