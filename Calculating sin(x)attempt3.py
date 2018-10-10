#Calculating the value of sin(x)    

import math
import sys

k = 0
x = float(input('Enter a value for x: '))
accuracy_value = 0.0000000001
numerator = 0
denominator = 0
term_value = 1
product = 1


while ( abs(term_value) >= accuracy_value ):
    term_value = term_value*((x*x)/((k+1)*(k+2)))
    # product = product*term_value
    print('the value of x is', repr(x))
    print('the value of the term is', repr(term_value))
    # print('the value of sine so far is', repr(product),'\n')
    k = k+2

print ( 'The value for sin',repr(x), 'is ',(repr(summation)),'\n')

