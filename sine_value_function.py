'''
Calculating the value of sin(x)    
'''

def sine_value(x):
    import math
    import sys
    k = 1
    accuracy_value = 0.00000000000000000001
    multiplier = 0
    summation=term_value=x
    while ( abs(term_value) >= accuracy_value ):
        multiplier = ((-1)*(x*x))/((k+1)*(k+2))
        term_value = term_value*multiplier
        summation = summation + term_value
        k = k+2
    print(repr(summation))

for i in range (100):
    print('The value of sin(', repr(i) , ' is ', sine_value(i))

