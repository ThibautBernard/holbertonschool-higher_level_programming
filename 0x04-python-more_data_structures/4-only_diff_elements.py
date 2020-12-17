#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    arr = []
    common = 0
    for i in set_1:
        common = 0
        for y in set_2:
            if i == y:
                common += 1
        if common == 0:
            arr.append(i)
    for t in set_2:
        common = 0
        for m in set_1:
            if t == m:
                common += 1
        if common == 0:
            arr.append(t)
    return arr
