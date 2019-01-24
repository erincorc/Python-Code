# GCD ITERATIVE AND RECURSIVE LAB

# ITERATIVE:
def gcditerative(num1, num2, x):
    if x == 0:
        gcd = 0
    for y in range(1,x+1): #need to add the +1 because range is not inclusive
        if num1%y == 0 and num2%y == 0:
            gcd = y
    return gcd

# RECURSIVE:
def gcdrecursive(num1, num2, x):
    if x == 0:
        gcd = 0
    elif num1%x == 0 and num2%x == 0:
        gcd = x
    else:
        return gcdrecursive(num1,num2,x-1)
    return gcd

num1 = 126
num2 = 999
x = min(num1,num2)
print "iterative: ", gcditerative(num1,num2,x)
print "recursive: ", gcdrecursive(num1,num2,x)


        
    
