'''
Practice for the Final
This file calculates the matrix trace and the antidiagonal
'''


from matrixfunctions import *

test_array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],
     [13,14,15,16]]
matrix_trace = 0
antidiagonal = 0
i = 0


def matrix_values(test_array):
    for i in range(rows(test_array)):
        matrix_trace = matrix_trace + test_array[i][i]
        antidiagonal = antidiagonal + test_array[i][(rows(test_array)) - 1 - i]

print (repr(matrix_trace))
print (repr(antidiagonal))
