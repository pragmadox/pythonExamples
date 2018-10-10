'''
Pattern the bounces of a ball
'''

import sys

def enter_height():
    h = float(input('Enter the height of the ball: '))
    while h <= 0:
        h = float(input('Enter the height of the ball: '))
    return h 

def enter_ratio():
    r = float(input('Enter the ratio between the height of each sequential bounce: '))
    while r <= 0 :
        r = float(input('Enter the ratio between each sequential bounce: '))
    return r

#enter_height()
#enter_ratio()


def bounce_distance():
    h = enter_height()
    r = enter_ratio()                  
    bounce = distance = h
    while bounce > sys.float_info.min: 
        bounce = bounce * r
        distance = distance + 2*bounce 
    print(repr(distance))
    

