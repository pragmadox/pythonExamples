# Jared Price
# July 9, 2015
# Python Class
# Temperature Conversion

#Temperature Conversion Program
#Fahrenheit to Celsius

#program greeting
print ('This program will convert from degrees Fahrenheit')
print (' to degrees Celsius.')

#get temperature in Fahrenheit
fahren = float(input('Enter degrees Fahrenheit: '))

#calculate degrees Celsuis
celsius = (fahren - 32) * 5 / 9

#output degrees Celsius
#print ( fahren, 'degrees Fahrenheit equals',
#   format( celsius, '.1f'), 'degrees Celsius' )
s = repr(fahren) + ' degrees Fahrenheit equals ' + \
    format ( celsius, '.1f' ) + ' degrees Celsius '
print (s)
