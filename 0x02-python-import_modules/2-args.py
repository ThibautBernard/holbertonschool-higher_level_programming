#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_arg = len(sys.argv) - 1
    if nb_arg == 0:
        print("{} arguments.".format(nb_arg))
    elif nb_arg == 1:
        print("{} argument:".format(nb_arg))
        print("{}: {}".format(nb_arg, sys.argv[1]))
    else:
        counter = 0
        print("{} arguments:".format(nb_arg))
        for i in sys.argv:
            if counter > 0:
                print("{}: {}".format(counter, i))
            counter += 1
