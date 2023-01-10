#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints integers of list,in reverse order"""

    my_list.reverse()
        for i in (len(my_list)):
            print("{:d}".format(my_list[i]))
