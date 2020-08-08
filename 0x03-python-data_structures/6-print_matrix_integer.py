#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in matrix:
        for integer in range(len(elem)):
            if integer < len(elem) - 1:
                print('{:d} '.format(elem[integer]), end='')
            else:
                print('{:d}'.format(elem[integer]), end='')
        print()
