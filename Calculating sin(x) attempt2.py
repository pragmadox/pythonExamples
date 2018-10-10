#Calculating the value of sin(x)    

import math
import sys

k = 0
x = float(input('Enter a value for x: '))
accuracy_value = 0.00000000000000001
numerator = 0
denominator = 0
term_value = 1
summation = 0



while ( abs(term_value) >= accuracy_value ):
    multiplier = (2*k+1)
    term_value = (((-1)**k)*(x**multiplier))/(math.factorial(multiplier))
    summation = summation + term_value 
    print('the value of x is', repr(x))
    print('the value of k is', repr(k))
    print('the value of the multiplier is', repr(multiplier))
    print('the value of the term is', repr(term_value))
    print('the value of the sum so far is', repr(summation),'\n')
    k = k+1

print ( 'The value for sin',repr(x), 'is ',(repr(summation)),'\n')

