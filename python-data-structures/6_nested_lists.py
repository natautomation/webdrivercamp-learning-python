#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def print_matrix(mtrx):
    for row in mtrx:
        for num in row:
            print(num, end=' ')
        print()


print_matrix(matrix)
