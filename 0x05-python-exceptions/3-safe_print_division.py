#!/usr/bin/python3
def safe_print_division(a, b):
    rest = None
    try:
        rest = (a / b)
        return rest
    except:
        return
    finally:
        print("Inside result: {}".format(rest))
