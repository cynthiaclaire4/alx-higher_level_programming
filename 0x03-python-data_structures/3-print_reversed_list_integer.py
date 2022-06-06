#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''prints all integer in reverse '''
    lc = len(my_list)
    for i in range(lc):
        print("{:d}".format(my_list[- i - 1]))
