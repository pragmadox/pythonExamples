#Countdown

n = 6 
def countdown(n):
    while n >= 0:
        if n != 0:
            print (repr(n) + '...',)
        else:
            print (repr(n))
        n = n - 1
countdown(n)
print (repr(n))
