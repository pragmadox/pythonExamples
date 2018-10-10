'''
This program will accept a given matrix, create a new matrix
and then tag positive values in the original matrix, assign
them to the same group in the new matrix with an ascending value, provided
the positive values reside directly to the sides, above, or below each other.
'''

from matrixfunctions_athome import *

test_matrix = read_matrix_data()

ordered_matrix = matrix_copy(test_matrix)

group_id = 2

print('Here is your original matrix: ')
print_matrix_table(test_matrix)
print('\n')

#Old function for recursive check
'''
def recurs_check( recurs_row, recurs_col, group_id ):
    if ordered_matrix[ recurs_row ][ recurs_col ] == 1:
        ordered_matrix[ recurs_row ][ recurs_col ] = group_id
        if recurs_row == ( columns( ordered_matrix ) - 1 ) \
        and recurs_col == ( rows( ordered_matrix ) - 1 ):
            recurs_check( recurs_row - 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col - 1, group_id )
        elif recurs_row == 0 and recurs_col == ( rows( ordered_matrix ) - 1 ):
            recurs_check( recurs_row, recurs_col - 1, group_id )
            recurs_check( recurs_row + 1, recurs_col, group_id )
        elif recurs_row == ( columns( ordered_matrix ) - 1 ) and recurs_col == 0:
            recurs_check( recurs_row - 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col + 1, group_id )
        elif recurs_row == 0 and recurs_col == 0:
            recurs_check( recurs_row + 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col + 1, group_id )
        elif recurs_row == 0:
            recurs_check( recurs_row, recurs_col - 1, group_id )
            recurs_check( recurs_row + 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col + 1, group_id )
        elif recurs_col == 0:
            recurs_check( recurs_row - 1, recurs_col, group_id )
            recurs_check( recurs_row + 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col + 1, group_id )
        else:
            recurs_check( recurs_row - 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col - 1, group_id )
            recurs_check( recurs_row + 1, recurs_col, group_id )
            recurs_check( recurs_row, recurs_col + 1, group_id )
'''

def recurs_check( ordered_matrix, recurs_row, recurs_col, group_id ):
    if ordered_matrix[ recurs_row ][ recurs_col ] == 1:
        ordered_matrix[ recurs_row ][ recurs_col ] = group_id
        if at_left_edge( recurs_row, recurs_col, ordered_matrix ) != True:
            recurs_check( ordered_matrix, recurs_row, recurs_col - 1, group_id )
        if at_top_edge( recurs_row, recurs_col, ordered_matrix ) != True:
            recurs_check( ordered_matrix, recurs_row - 1, recurs_col, group_id )
        if at_right_edge( recurs_row, recurs_col, ordered_matrix ) != True:
            recurs_check( ordered_matrix, recurs_row, recurs_col + 1, group_id )
        if at_bottom_edge( recurs_row, recurs_col, ordered_matrix ) != True:
            recurs_check( ordered_matrix, recurs_row + 1, recurs_col, group_id )
            
                  
#possible conditions earlier explored
'''
            if ( recurs_row -1) >= 0:
                recurs_check( recurs_row - 1, recurs_col, group_id )
            if ( recurs_col - 1) >= 0:
                recurs_check( recurs_row, recurs_col - 1, group_id )
            if ( recurs_row + 1) < columns( ordered_matrix ): 
                recurs_check( recurs_row + 1, recurs_col, group_id )
            if ( recurs_col + 1 ) < rows( ordered_matrix ):
                recurs_check( recurs_row, recurs_col + 1, group_id )
'''        

def begin_proc( ordered_matrix ):
    curr_row, curr_col, group_id = 0, 0, 2
    while ordered_matrix[ curr_row ][ curr_col ] == 0:
        if ordered_matrix[ curr_row ][ curr_col ] == 0 \
                and at_right_edge( curr_row, curr_col, ordered_matrix ) == True:
            curr_row = curr_row + 1
        curr_col = curr_col + 1
    return curr_row, curr_col, group_id

def graduate_val( curr_row, curr_col, ordered_matrix, group_id ):
    while ordered_matrix[ curr_row ][ curr_col ] != 1 \
          and curr_row < rows( ordered_matrix )\
          and curr_col < columns( ordered_matrix ):
        if ordered_matrix[ curr_row ][ curr_col ] != 1 \
           and at_right_edge( curr_row, curr_col, ordered_matrix ) == True:
            curr_row = curr_row + 1
            curr_col = 0
        else:
            curr_col = curr_col + 1
    recurs_row, recurs_col = curr_row, curr_col
    recurs_check( ordered_matrix, recurs_row, recurs_col, group_id )
    return curr_row, curr_col, group_id


'''
def graduate_values( current_column, current_row ): 
    if current_column < columns(ordered_matrix) and current_row < rows(ordered_matrix):
        current_column = current_column + 1
        if current_column == ( columns(ordered_matrix) - 1 ):
            current_column = 0
            current_row =  current_row + 1        
'''
      
curr_row, curr_col, group_id = begin_proc( ordered_matrix )
recurs_check ( ordered_matrix, curr_row, curr_col, group_id )
while any( 1 in subl for subl in ordered_matrix ) == True:
    graduate_val( curr_row, curr_col, ordered_matrix, group_id )
    group_id = group_id + 1
   
print('Here is the ordered matrix: ')
print_matrix_table(ordered_matrix)
print('\n')

print('Here are the values closer together: ')
print_close_matrix(ordered_matrix)
