s=open("./input/98.txt").readline()
##########################################################################################
from itertools import permutations
from math import isqrt

a=s.split('\",\"')
a[0]=a[0][1:]
a[-1]=a[-1][:-1]

S,T={},{}
for i in a:
    rep=''.join(sorted(i))
    if rep not in S: S[rep]=[]
    S[rep].append(i)
    if len(S[rep])>1: T[rep]=S[rep]

ans=0
for k in T:
    if len(str(ans))>len(k): continue
    for p in permutations([9,8,7,6,5,4,3,2,1,0], len(k)):
        m,x,v=dict(zip(sorted(list(set(k))), p)),0,0
        for s in T[k]:
            if m[s[0]]==0: continue
            t=int(''.join([str(m[c]) for c in s]))
            if isqrt(t)**2==t:
                v,x=max(v, t),x+1
        if x>1: ans=max(ans, v)
print(ans)