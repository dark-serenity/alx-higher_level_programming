#!/usr/bin/python3

def print_list_integer(my_list=[]):
    my_list = [1, 2, 3, 4, 5]

# Assign individual elements from the list to variables
first_element = my_list[0]
second_element = my_list[1]
third_element = my_list[2]
fourth_element = my_list[3]
fifth_element = my_list[4]

# Print the formatted values of the first five elements
print("{:d}".format(first_element))
print("{:d}".format(second_element))
print("{:d}".format(third_element))
print("{:d}".format(fourth_element))
print("{:d}".format(fifth_element))
