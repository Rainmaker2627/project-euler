L=12000
##########################################################################################
from math import isqrt, prod, inf
import heapq

m=[inf]*(L+1)
m[0]=m[1]=0
bfs=[(4, [2, 2])]
while len(bfs)>0:
    p,l=heapq.heappop(bfs)
    while len(bfs)>0 and (p,l)==bfs[0]:
        heapq.heappop(bfs)
    m[p-sum(l)+len(l)]=min(m[p-sum(l)+len(l)], p)
    t=[l+[2]]
    for i in range(len(l)):
        f=sorted([l[j]+(1 if j==i else 0) for j in range(len(l))], reverse=True)
        if f not in t: t.append(f)
    for i in t:
        if prod(i)-sum(i)+len(i)<=L:
            heapq.heappush(bfs, (prod(i), i))
print(sum(set(m)))