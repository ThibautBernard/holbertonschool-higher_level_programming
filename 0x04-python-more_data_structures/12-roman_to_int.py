#!/usr/bin/python3
def roman_to_int(roman_string):
    dico = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    last = 0
    count = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    for i in range(len(roman_string)):
        for r, v in dico.items():
            if roman_string[i] == r:
                sum += v
                if count == 0:
                    last = v
                    count += 1
                if last < v:
                    sum -= 2
                if count != 0:
                    last = v
    return sum
