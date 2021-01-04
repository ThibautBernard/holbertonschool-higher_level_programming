#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if (value <= 0 or value >= 0):
            print("{:d}".format(value))
            return True
    except Exception as n:
        print("Exception: {}".format(n), file=sys.stderr)
