#Useful List Functions

def say_hello():
    print ('Welcome to the final project')
    print 

def say_goodbye():
    print ('Goodbye to the final project')
    print

b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def columns ( b ):
    return len( b[0] )

def rows( b ):
    return len( b )

def print_matrix( b ):
    for row in range( rows( b )):
        for col in range( columns( b )):
            print ('%1d' %b[row][col], end = ' ',)
        print (' ')

def at_right_edge( row, col, b ):
    return col == max( range( columns( b )))

def at_bottom_edge( row, col, b ):
    return row == max( range( rows( b )))

def at_left_edge( row, col, b ):
    return col == 0

def at_top_edge( row, col, b ):
    return row == 0

def matrix_copy( b ):
    c = []
    for row in range( len(b)):
        lst = []
        for col in range( len( b[row] )):
            lst.append( b[row][col] )
        c.append(lst)
        print ('row %d of the new matrix' %row)
        print_matrix(c)
    return c

def read_matrix_data():
    file_name = input( 'Enter data file name: ')
    input_file = \
    open( 'C:/Users/J.X/Google Drive/Files and Documents/Academic/Fordham University/Summer 2015/Programming with Python/' + file_name, 'r')
    test_matrix = []
    empty_str = ''

    line = input_file.readline()
    while line != empty_str:
        lst = line.split()
        for i in range ( len( lst ) ):
            lst[i] = int( lst[i] )
        test_matrix.append( lst )
        line = input_file.readline()

    input_file.close()

def matrix_trace(b):
    trace_value = 0
    for i in range(len(b)):
        trace_value = trace_value + b[i][i]
    return trace_value    
