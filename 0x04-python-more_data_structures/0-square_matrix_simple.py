#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    arr = []
    counter = 0
    for i in matrix:
        arr_row = []
        for x in i:
            arr_row.append(x * x)
        arr.append(arr_row)
    return arr
