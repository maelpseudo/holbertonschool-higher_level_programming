#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result_matrix = [row[:] for row in matrix]

    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[i])):
            result_matrix[i][j] = result_matrix[i][j] ** 2

    return result_matrix
