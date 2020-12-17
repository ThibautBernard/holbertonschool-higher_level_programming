#!/usr/bin/python3
def uniq_add(my_list=[]):
    arr = []
    occ = 0
    sum = 0
    if len(my_list) == 0:
        return 0
    arr.append(my_list[0])
    for i in my_list:
        occ = 0
        for y in arr:
            if i == y:
                occ += 1
                break
        if occ == 0:
            arr.append(i)
    for z in arr:
        sum += z
    return sum
