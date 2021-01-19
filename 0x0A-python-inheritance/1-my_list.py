#!/usr/bin/python3
""" subclass of class list """


class MyList(list):
    """ class inerihted from list class """
    def print_sorted(self):
        """ print in a sorted way the list """
        list_cp = sorted(self[:])
        print(list_cp)
