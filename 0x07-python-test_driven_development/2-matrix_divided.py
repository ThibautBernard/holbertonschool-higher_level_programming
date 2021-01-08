#!/usr/bin/python3
"""
matrix_divided - div matrix number

"""


def matrix_divided(matrix, div):
    """ function that div number of the matrix
    Args:
        matrix: (list of lists): a matrix of integer
        div: (int, float): number to be divised with

    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    len_prev_row = 0
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    count_row = 0
    count_height = 0
    if matrix is None:
        raise TypeError(err_msg)
    mc = list(map(list, matrix))
    t = 0
    len_prev_row = len(mc[0])
    for i in mc:
        if count_height > 0:
            t = len_prev_row
            len_prev_row = len(i)
        else:
            t = len_prev_row
        count_row = 0
        for y in i:
            if y == 0:
                raise ZeroDivisionError("division by zero")
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError(err_msg)
            else:
                mc[count_height][count_row] = round(y / div, 2)
            count_row += 1
        count_height += 1
        if t != len_prev_row:
            raise TypeError("Each row of the matrix must have the same size")
    return mc
