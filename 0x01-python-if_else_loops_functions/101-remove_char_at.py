#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    count = 0
    for i in range(len(str)):
        if (count != n):
            strcpy = strcpy + str[i]
        count += 1
    return strcpy
