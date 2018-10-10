'''
This function computes the sum of 1 + 1/4 + 1/9 + .... 1/n^2.
'''

def recursing(n):
    if n == 1:
        return 1
    else:
        return (1/(n*n)) + recursing(n-1)
