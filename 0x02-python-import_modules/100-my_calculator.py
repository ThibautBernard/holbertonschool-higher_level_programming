#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    nb_arg = len(sys.argv)
    counter = 0
    sum = 0
    nb_arg -= 1
    if nb_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    first = int(sys.argv[1])
    operator = sys.argv[2]
    second = int(sys.argv[3])
    if operator == "+":
        print("{} + {} = {}".format(first, second, add(first, second)))
    elif operator == "-":
        print("{} - {} = {}".format(first, second, sub(first, second)))
    elif operator == "/":
        print("{} / {} = {}".format(first, second, div(first, second)))
    elif operator == "*":
        print("{} * {} = {}".format(first, second, mul(first, second)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
