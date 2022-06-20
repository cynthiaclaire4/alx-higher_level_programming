#!/usr/bin/python3
# a function that prints an integer with "{c:d}".format()


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return(False)
    else:
        return(True)