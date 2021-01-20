#!/usr/bin/python3
"""function that define a pascal triangle"""


def pascal_triangle(n):
    """ triangle pascal function """
    if n <= 0:
        return []
    p = [[1]]
    for i in range(1, n):
        m = [1]
        for y in range(1, i):
            """print("->{} et ->{}".format(tri[i-1][y-1], tri[i-1][y]))"""
            m.append(p[i-1][y-1] + p[i-1][y])
        m.append(1)
        p.append(m)
    return p
