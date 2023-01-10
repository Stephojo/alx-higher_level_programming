i!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces element of list at specific position"""
    
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
