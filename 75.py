N=1500000
##########################################################################################
from math import isqrt, gcd

t=isqrt(N)
prim,all=[0]*(N+1),[0]*(N+1)
for p in range(1, t):
    for q in range(p%2+1, p, 2):
        if gcd(p, q)!=1: continue
        if 2*p*(p+q)>N: break
        prim[2*p*(p+q)]+=1

tot=0
for i in range(1, N+1):
    for j in range(i, N+1, i):
        all[j]+=prim[i]
    if all[i]==1: tot+=1
print(tot)