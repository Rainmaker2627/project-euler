N=20
##################
from math import gcd

l=1
for i in range(2, N+1):
    l=l*i//gcd(l, i)
print(l)