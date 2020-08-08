#!/usr/bin/python3
"""
matrix: matrix must be a list of lists of integers or floats
div: All elements of the matrix should be divided by div
"""


def matrix_divided(matrix, div):
    """ matrix_divided: divides all elements of a matrix. """
    result = eval(repr(matrix))
    for items in matrix:
        if len(items) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for List in range(len(result)):
        for element in range(len(result[List])):
            if not isinstance(result[List][element], int):
                if not isinstance(result[List][element], float):
                    raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")
            elif isinstance(result[List][element], int):
                result[List][element] = result[List][element] / div
                result[List][element] = round(result[List][element], 2)
            elif isinstance(result[List][element], float):
                result[List][element] = result[List][element] / div
                result[List][element] = round(result[List][element], 2)
    return result
