'''
This program will accept a given matrix, create a new matrix
and then tag positive values in the original matrix, assign
them to the same group in the new matrix with an ascending value, provided
the positive values reside directly to the sides, above, or below each other.
'''

from matrixfunctions_athome import *

test_matrix = read_matrix_data()

ordered_matrix = matrix_copy(test_matrix)

print('Here is your original matrix: ')
print_matrix(test_matrix)

#Old function for recursive check
'''
def recurs_check( recursion_row, recursion_col, group_id ):
    if test_matrix[ recursion_row ][ recursion_col ] == 1:
        ordered_matrix[ recursion_row ][ recursion_col ] = group_id
        if recursion_row == ( columns( test_matrix ) - 1 ) \
        and recursion_col == ( rows( test_matrix ) - 1 ):
            recurs_check( recursion_row - 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col - 1, group_id )
        elif recursion_row == 0 and recursion_col == ( rows( test_matrix ) - 1 ):
            recurs_check( recursion_row, recursion_col - 1, group_id )
            recurs_check( recursion_row + 1, recursion_col, group_id )
        elif recursion_row == ( columns( test_matrix ) - 1 ) and recursion_col == 0:
            recurs_check( recursion_row - 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col + 1, group_id )
        elif recursion_row == 0 and recursion_col == 0:
            recurs_check( recursion_row + 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col + 1, group_id )
        elif recursion_row == 0:
            recurs_check( recursion_row, recursion_col - 1, group_id )
            recurs_check( recursion_row + 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col + 1, group_id )
        elif recursion_col == 0:
            recurs_check( recursion_row - 1, recursion_col, group_id )
            recurs_check( recursion_row + 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col + 1, group_id )
        else:
            recurs_check( recursion_row - 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col - 1, group_id )
            recurs_check( recursion_row + 1, recursion_col, group_id )
            recurs_check( recursion_row, recursion_col + 1, group_id )
'''

def recurs_check( test_matrix, recursion_row, recursion_col, group_id ):
    if test_matrix[ recursion_row ][ recursion_col ] == 1:
        ordered_matrix[ recursion_row ][ recursion_col ] = group_id
        if at_left_edge( recursion_row, recursion_col, test_matrix ) != True:
            recurs_check( test_matrix, recursion_row, recursion_col - 1, group_id )
        if at_top_edge( recursion_row, recursion_col, test_matrix ) != True:
            recurs_check( test_matrix, recursion_row - 1, recursion_col, group_id )
        if at_right_edge( recursion_row, recursion_col, test_matrix ) != True:
            recurs_check( test_matrix, recursion_row, recursion_col + 1, group_id )
        if at_bottom_edge( recursion_row, recursion_col, test_matrix ) != True:
            recurs_check( test_matrix, recursion_row + 1, recursion_col, group_id )
        
                  
#possible conditions earlier explored
'''
            if ( recursion_row -1) >= 0:
                recurs_check( recursion_row - 1, recursion_col, group_id )
            if ( recursion_col - 1) >= 0:
                recurs_check( recursion_row, recursion_col - 1, group_id )
            if ( recursion_row + 1) < columns( test_matrix ): 
                recurs_check( recursion_row + 1, recursion_col, group_id )
            if ( recursion_col + 1 ) < rows( test_matrix ):
                recurs_check( recursion_row, recursion_col + 1, group_id )
'''        

def begin_proc( test_matrix ):
    curr_row, curr_col = 0, 0
    group_id = 2
    while test_matrix[ curr_row ][ curr_col ] == 0:
        if test_matrix[ curr_row ][ curr_col ] == 0 \
                and at_right_edge( curr_row, curr_col, test_matrix ) == True:
            curr_row = curr_row + 1
        curr_col = curr_col + 1
    return curr_row, curr_col, group_id

def graduate_val( curr_row, curr_col, test_matrix, group_id ):
    while test_matrix[ curr_row ][ curr_col ] != 1 \
          and curr_row < rows( test_matrix )\
          and curr_col < columns( test_matrix ):
        if test_matrix[ curr_row ][ curr_col ] != 1 \
           and at_right_edge( curr_row, curr_col, test_matrix ) == True:
            curr_row = curr_row + 1
            curr_col = 0
        curr_col = curr_col + 1
    recursion_row, recursion_col = curr_row, curr_col
    recurs_check( test_matrix, recursion_row, recursion_col, group_id )
    group_id = group_id + 1
    return curr_row, curr_col, group_id


'''
def graduate_values( current_column, current_row ): 
    if current_column < columns(test_matrix) and current_row < rows(test_matrix):
        current_column = current_column + 1
        if current_column == ( columns(test_matrix) - 1 ):
            current_column = 0
            current_row =  current_row + 1        
'''
      
curr_row, curr_col, group_id = begin_proc( test_matrix )
recurs_check ( test_matrix, curr_row, curr_col, group_id )
while any( 1 in subl for subl in ordered_matrix ) == True:
    curr_row, curr_col, group_id = graduate_val ( curr_row, curr_col, test_matrix, group_id )

print('Here is the ordered matrix: ')
print_matrix(ordered_matrix)
