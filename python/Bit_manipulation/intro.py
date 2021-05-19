def solve(number):
    while number > 0:
        binary_str = ""
        rem = number % 2
        binary_str += str(rem)
        number //= 2

    return binary_str[::-1]


if __name__ == "__main__":
    print(solve(155))
