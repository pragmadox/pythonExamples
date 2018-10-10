'''
Calculating the value of sin(x)    
'''

import math
import sys

k = 1
x = term_value = summation = float(input('Enter a value for x: '))
accuracy = 0.000000000000001
numerator = 0
denominator = 0
multiplier = 0

while ( abs(term_value) >= accuracy ):
    multiplier = ((-1)*(x*x))/((k+1)*(k+2))
    term_value = term_value*multiplier
    summation = summation + term_value
    k = k+2
    
print('the value of x is', repr(x))
print('the value of k is', repr(k))
print('the value of the term is', repr(term_value))
print('the value of the sum so far is', repr(summation),'\n')
print( 'The value for sin',repr(x), 'is ',(repr(summation)),'\n')

