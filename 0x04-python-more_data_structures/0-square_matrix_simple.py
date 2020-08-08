#!/usr/bin/python3
# function that computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    new_matrix = []

    def square(number): return number ** 2
    for column in matrix:
        new_matrix.append(list(map(square, column)))

    return new_matrix
