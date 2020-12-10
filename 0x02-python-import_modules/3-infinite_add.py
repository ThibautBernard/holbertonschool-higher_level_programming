#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_arg = len(sys.argv)
    counter = 0
    sum = 0
    nb_arg -= 1
    for i in sys.argv:
        if counter > 0:
            sum += int(i)
        counter += 1
    print("{}".format(sum))
