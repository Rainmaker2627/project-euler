N=10001
##################
from math import log

hi=int(N*(log(N)+log(log(N))))
p,l=[1]*(hi+1),[]
p[0]=p[1]=0
for i in range(2, hi+1):
    if p[i]==0:
        continue
    l.append(i)
    if len(l)==N:
        print(i)
        break
    for j in range(i*i, hi, i):
        p[j]=0