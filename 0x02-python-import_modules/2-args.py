#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_arg = len(sys.argv)
    if nb_arg == 1:
        print("0 arguments.")
    elif nb_arg == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        counter = 0
        nb_arg -= 1
        print("{} arguments: ".format(nb_arg))
        for i in sys.argv:
            if counter > 0:
                print("{}: {}".format(counter, i))
        counter += 1
