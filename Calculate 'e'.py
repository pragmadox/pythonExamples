# Calculate e

import math
import sys

i = 0
sum = 1
x = int(input('Enter a value for x: '))
accuracy = .000000001    
term = 1

while abs(term) >(accuracy):
    term = term * (x/(i+1))
    sum = sum + term
    i = i+1

print (repr(sum))

