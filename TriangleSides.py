# Jared Price
# July 9, 2015
# Python Class
# Temperature Conversion

import math

'''
This program checks whether three lengths can belong
to the three sides of a triangle
'''

SideA = float(input('Enter the length of side A: '))
SideB = float(input('Enter the length of side B: '))
SideC = float(input('Enter the length of side B: '))

halfperimeter = ( SideA + SideB + SideC ) / 2

if ( ( SideA + SideB > SideC ) and ( SideB + SideC > SideA) \
    and ( SideA + SideC > SideB ) ):

    #Calculate the area of the triangle

    Area = math.sqrt( halfperimeter*(halfperimeter-SideA)*(halfperimeter-SideB)*(halfperimeter-SideC) )

    print (Area)
    
else:

    print ( 'The values of these numbers cannot represent the sides of a triangle.' )
            
    
    
