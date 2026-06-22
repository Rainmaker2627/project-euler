L=1000000
##########################################################################################
from math import isqrt

m,s=1,0
while s<L:
    for a in range(1, 2*m):
        r=a**2+m**2
        if isqrt(r)**2==r:
            s+=min(a, m-1)-(a+1)//2+1
    m+=1
print(m)