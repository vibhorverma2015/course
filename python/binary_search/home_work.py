"""
find he number of times the target occured in the array with 
lower bound and upper bound 
"""

# by normal and basic way:

from typing import Counter


a = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 8, 8, 8, 9, 9]
target = 6


def number_of_targets(a, target):
    prev = 1
    cnt = 0
    for i in range(0, len(a)):
        if a[i] == target:
            cnt += 1
            return i
        else:
            if a[i] != target:
                return i
            prev = i


if __name__ == "__main__":
    a = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 8, 8, 8, 9, 9]
    target = 6

    print(number_of_targets(a, target))
