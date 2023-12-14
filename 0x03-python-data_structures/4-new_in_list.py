#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()  # Return a copy of the original list if index is out of bounds
    my_list[idx] = element
    return my_list.copy()  # Return a copy of the modified list
