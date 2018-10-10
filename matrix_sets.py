'''
matrix_sets.py
'''

from matrixfunctions import print_matrix

def read_matrix_data():
    file_name = input( 'Enter data file name: ')
    input_file = \
    open( 'C:/Users/J.X/Google Drive/Files and Documents/Academic/Fordham University/Summer 2015/Programming with Python/' + file_name, 'r')
    a = []
    empty_str = ''

    line = input_file.readline()
    while line != empty_str:
        lst = line.split()
        for i in range ( len( lst ) ):
            lst[i] = int( lst[i] )
        a.append( lst )
        line = input_file.readline()

    input_file.close()
    return a

test_matrix = read_matrix_data()

