#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Check if the search value is present in the list
    if search in my_list:
        # Replace the search value with the replace value
        index = my_list.index(search)
        my_list[index] = replace
