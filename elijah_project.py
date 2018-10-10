def say_hello():
    print 'Welcome to the project'
    print

def say_goodbye():
    print 'Goodbye to the project'
    print

def columns(b):
    return len(b[0])

def rows(b):
    return len(b)

def print_matrix(b):
    for row in range(rows(b)):
        for col in range(columns(b)):
            print '%2d' %b[row][col],
        print

def at_right_edge(row,col,b):
    return col == max(range(columns(b)))

def at_bottom_edge(row,col,b):
    return row == max(range(rows(b)))

def at_left_edge(row,col,b):
    return col == 0

def at_top_edge(row,col,b):
    return row == 0

def matrix_copy(b):
    c = []
    for row in range(len(b)):
        lst = []
        for col in range(len(b[row])):
            lst.append(b[row][col])
        c.append(lst)
        print 'row %d of the new matrix' %row
        print_matrix(c)
    return c

def read_matrix_data():
    file_name = 'matrix.dat'
    input_file = \
    open( 'D:/Google Drive/Files and Documents/Academic/Fordham University/Summer 2015/Programming with Python/'+file_name, 'r' )
    a = []
    empty_str = ''
    line = input_file.readline()
    while line != empty_str:
        lst = line.split()
        for i in range( len(lst)):
            lst[i] = int(lst[i])
        a.append(lst)
        line = input_file.readline()
    input_file.close()
    return a

def start(b):
    marki, markj = 0, 0
    while b[marki][markj] == 0:
        if b[marki][markj] == 0 and at_right_edge(marki,markj,b) == True:
            marki = marki + 1
        markj = markj + 1
    return marki, markj

def move_on(marki, markj, b, sol_num):
    while b[marki][markj] != 1 and marki < num_rows and markj < num_cols:
        if b[marki][markj] != 1 and at_right_edge(marki,markj,b) == True:
            marki = marki + 1
            markj = 0
        else:
            markj = markj + 1
    tempi, tempj = marki, markj
    check(b,sol_num,marki,markj)
    return marki, markj

def check(b,sol_num, marki, markj):
    if b[marki][markj] == 1:
        b[marki][markj] = sol_num
    if at_top_edge(marki,markj,b) == False:
        if b[marki - 1][markj] == 1:
            b[marki-1][markj] = sol_num
            check(b,sol_num, marki-1,markj)
    if at_bottom_edge(marki,markj,b) == False:
        if b[marki + 1][markj] == 1:
            b[marki + 1][markj] = sol_num
            check(b,sol_num, marki+1,markj)
    if at_right_edge(marki,markj,b) == False:
        if b[marki][markj + 1] == 1:
            b[marki][markj + 1] = sol_num
            check(b,sol_num, marki,markj+1)
    if at_left_edge(marki,markj,b) == False:
        if b[marki][markj - 1] == 1:
            b[marki][markj - 1] = sol_num
            check(b,sol_num, marki,markj-1)

b = read_matrix_data()
print 'Original Matrix'
print_matrix(b)
print ''

num_rows = rows(b)
num_cols = columns(b)
sol_num = 2

marki, markj = start(b)
check(b, sol_num, marki, markj)
n = 1
while any(1 in subl for subl in b) == True:
    marki, markj = move_on(marki, markj, b, sol_num+n)
    n = n+1

print 'Matrix with Groups Identified'
print_matrix(b)
