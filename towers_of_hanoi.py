source = 0;
auxiliary = 1;
destination = 2;

def towers_of_hanoi( n, source, auxiliary, destination):
    if n > 0:
        towers_of_hanoi( n-1, source, destination, auxiliary);
        move_disk( source, destination );
        towers_of_hanoi( n-1, auxiliary, source, destination);

def move_disk ( fromm, to ):
    print ('Move the top disk from ',)
    write_peg( fromm ),
    print (' to ',)
    write_peg( to ),
    print ('\n')

def write_peg ( p ):
    if p == 0:
        print(' source ')
    if p == 1:
        print(' auxiliary ')
    if p == 2:
        print(' destination ')

print
number_of_disks = int(input(' Enter the number of disks: '))

print
print ('    Instructions \n\n')

towers_of_hanoi( number_of_disks, source, auxiliary, destination );

print 
