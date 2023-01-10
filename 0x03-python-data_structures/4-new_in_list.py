#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ function replaces an element in a list without
    modifying original"""

    if idx < 0 and idx > len(my_list) - 1:
        return my_list
    else:
        anotherList = my_list.copy()
        anotherList[idx] = element
        return anotherList
