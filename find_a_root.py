def sign(x):
    if x >= 0:
        return +1
    else:
        return -1

def y(x):
    return x**3 - 10*x - 40

def rootfinder(a, b):
    accuracy = 1e-10
    left = a
    right = b
    midpoint = (left+right)/2
    while abs(y(midpoint)) >= accuracy:
        midpoint = (left+right)/2
        if sign(y(left)) == sign(y(midpoint)):
            left = midpoint
        if sign(y(right)) == sign(y(midpoint)):
            right = midpoint
    print( repr(midpoint))



        
