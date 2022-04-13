"""
Name: Lexie DelViscio
algorithms.py

Problem: This program contains multiple functions that operate by
utilizing while loops, list methods, and conditional statements.
It has functions to read in numbered data from a file and return
a list of that data, and to determine using a linear search if a
value is contained in a list.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(filename):
    my_list = []
    in_file = open(filename, 'r')
    entire_file = in_file.read()
    words = entire_file.split()
    i = 0
    while i < len(words):
        nums = eval(words[i])
        my_list += [nums]
        i += 1
    in_file.close()
    return my_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if values[i] == search_val:
            return True
        i += 1
    return False


if __name__ == '__main__':
    pass
