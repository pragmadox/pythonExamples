'''
The object of this exercise is to write a program that produces a table
of Celsius equivalents to the Fahrenheit degrees between 10 and 100 degrees
Fahrenheit with the step of 10.
'''

from matrixfunctions_atschool import *

def cels(fahren):
    celsius = (fahren - 32) * 5 / 9
    return celsius

temp_table = []

for i in range( 10, 100, 10 ):
    temp_table.append([i, cels(i)])

print ('  Celsius      Fahrenheit')   
print_matrix_table(temp_table)  

