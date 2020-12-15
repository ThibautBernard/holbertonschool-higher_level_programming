#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    lenth_line = len(matrix[0])
    counter = 0
    c = 0
    for i in matrix:
        lenth_line = len(matrix[counter])
        c = 0
        for x in i:
            if c < lenth_line - 1:
                print("{:d}".format(x), end=" ")
            else:
                print("{:d}".format(x), end="")
            c += 1
        print()
        counter += 1
