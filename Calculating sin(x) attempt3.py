#Calculating the value of sin(x)    

import math
import sys

k = 1
x = term_value = summation = float(input('Enter a value for x: '))
accuracy_value = 0.000001
numerator = 0
denominator = 0
multiplier = 0

while ( abs(term_value) >= accuracy_value ):
    term_value = term_value*((-1)*((x*x)/((2*k)*(2*k+1))))
    summation = summation + term_value
    print('the value of x is', repr(x))
    print('the value of k is', repr(k))
    print('the value of the term is', repr(term_value))
    print('the value of the sum so far is', repr(summation),'\n')
    k = k+1

print ( 'The value for sin',repr(x), 'is ',(repr(summation)),'\n')

