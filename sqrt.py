# sqrt.py
# Routines for computing squqre roots to high precision
# Ronald L. Rivest, for 6.006 Introduction to Algorithms
# 10/15/12

def newtonsqrt(a, x = 1):
    """ Use Newton's method to compute floor(sqrt(a)), with x as first guess """
    while True:
        if x**2 <= a and (x+1)**2 > a:
            return x
        x = (x + a // x) // 2

def sqrt(a, d):
    """ 
    Compute sqrt(a) to at least d-digit precision (i.e. sqrt(a*10**2d));
    this represents d significant digits after decimal point.
    """
    return newtonsqrt(a*10**(2*d), 10**d)

def sqrtx(a, d):
    """ Same, but increase d as we go, to improve speed """
    if d<10:
        return newtonsqrt(a*10**(2*d), 10**d)
    prec = d // 2
    x = sqrtx(a, prec)
    return newtonsqrt(a*10**(2*d), x*10**(d-prec))

# compute million-digit precision for sqrt(2), then take last 10 digits only
print (sqrtx(2,1000000) % (10**5))

# Last 10 digits of the million digits after decimal point
# in sqrt(2) are 9048412043
# so "3" is the "millionth digit" of sqrt(2).

# This takes about 45 seconds on my macbook air.  
