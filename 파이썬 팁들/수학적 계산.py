# nCr
import math
def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))

print(nCr(4,2))