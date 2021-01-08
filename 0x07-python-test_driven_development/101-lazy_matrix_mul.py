"""
lazy_matrix_mul - multiplication matrix

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ function that multiply two matrix into one using module numpy

    Args:
        m_a: (list of lists): list of lists of integer
        m_b: (list of lists): list of lists of integer
     """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not any(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not any(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if all([not elem for elem in m_a]):
        raise ValueError("m_a can't be empty")
    if all([not elem for elem in m_b]):
        raise ValueError("m_b can't be empty")
    current_r_a = 0
    prev_r_a = 0
    counter_a = 0
    for t in m_a:
        current_r_a = len(t)
        if current_r_a != prev_r_a and counter_a != 0:
            raise TypeError("each row of m_a must be of the same size")
        for l in t:
            if not isinstance(l, int) and not isinstance(l, float):
                raise TypeError("m_a should contain only integers or floats")
        prev_r_a = current_r_a
        counter_a += 1
    curr_r_b = 0
    prev_r_b = 0
    counter_b = 0
    for z in m_b:
        curr_r_b = len(z)
        if curr_r_b != prev_r_b and counter_b != 0:
            raise TypeError("each row of m_b must be of the same size")
        for o in z:
            if not isinstance(o, int) and not isinstance(o, float):
                raise TypeError("m_b should contain only integers or floats")
        prev_r_b = curr_r_b
        counter_b += 1
    try:
        res = np.dot(m_a, m_b)
    except:
        raise ValueError("m_a and m_b can't be multiplied")
    return res
