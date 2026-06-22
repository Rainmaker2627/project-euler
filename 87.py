L=50000000
##########################################################################################
from math import isqrt

s=0
sq=[0]*(L+1)
sqrt=isqrt(L)
lp,pr=[0]*(sqrt+1),[]
for i in range(2, sqrt+1):
    if lp[i]==0:
        lp[i]=i
        sq[i*i]=1
        pr.append(i)
    j=0
    while j<len(pr) and i*pr[j]<=sqrt:
        lp[i*pr[j]]=pr[j]
        if pr[j]==lp[i]:
            break
        j+=1

S=set()
for i in pr:
    for j in pr:
        for k in pr:
            if i**2+j**3+k**4>L:
                continue
            S.add(i**2+j**3+k**4)
print(len(S))