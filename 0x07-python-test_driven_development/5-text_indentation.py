#!/usr/bin/python3
"""
print_square - print a square

"""

def text_indentation(text):
    """ function that print a square from size """
    signal = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delim = ['?', '.', ':']
    tmp = []
    st = ""
    tmp_prev = ""
    for i in text:
        tmp.append(i)
        for y in delim:
            if i == y:
                for o in tmp:
                    o = o.replace(' ', '')
                    print(o, end="")
                signal = 1
                del tmp[:]
                tmp_prev = i
                print()
                print()
    for ded in tmp:
        ded = ded.replace(' ', '')
        print(ded, end="")
