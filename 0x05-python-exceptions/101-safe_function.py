#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as n:
        print("Exception: {}".format(n), file=sys.stderr)
        return None
