#!/usr/bin/python3
for x in range(0, 10):
    for i in range(0, 10):
        if i > x:
            print("{:d}".format(x), end="");
            if x + i != 17:
                print("{:d}".format(i), end=", ");
            else:
                print("{:d}".format(i));
