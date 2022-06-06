#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''prints all integer in reverse '''
    if (my_list):
        rev = my_list[::-1]
        for i in rev:
            print("{:d}".format(my_list[i]))
