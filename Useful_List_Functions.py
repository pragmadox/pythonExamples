#Useful List Functions

def say_hello():
    print ('Welcome to the final project')
    print 

def say_goodbye():
    print ('Goodbye to the final project')
    print

b = [[1,2,3,4],[5,6,7,8]]

def columns ( b ):
    return len( b[0] )

def rows( b ):
    return len( b )

def print_matrix( b ):
    for row in range( rows( b )):
        for col in range( columns( b )):
            print ('%1d' %b[row][col],)
        print

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

