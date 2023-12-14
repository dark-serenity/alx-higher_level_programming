def print_list_integer(my_list=[]):
    for number in my_list:
        print("{:d}".format(number))

# Test the function with the provided example
my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
