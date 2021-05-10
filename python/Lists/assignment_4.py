number_of_rows = int(input())

for rows in range(0, number_of_rows + 1):
    for number_of_stars in range(rows):
        print("*", end=" ")

    print()
