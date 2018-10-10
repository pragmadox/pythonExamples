import random
import math

inside = 0
length = 0
total = 1000000

for num in range(1000000):
    x = random.random()
    y = random.random()
    length = math.sqrt(x**2 + y**2)
    if length <= 1:
        inside = inside+1
    print (repr(inside/total))

pi = 4*(inside/total)
print(repr(pi))

 
