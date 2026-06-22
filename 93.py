from itertools import permutations, combinations_with_replacement
from fractions import Fraction
from math import inf

S={}
op=[lambda a,b: a+b, lambda a,b: inf if a==inf or b==inf else a-b, lambda a,b: inf if a==inf or b==inf else a*b, lambda a,b: inf if b==0 or b==inf or a==inf else Fraction(a, b)]
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                rep=tuple(sorted([a,b,c,d]))
                if rep not in S: S[rep]=[]
                for x in combinations_with_replacement([0,1,2,3], 3):
                    for y in permutations(x):
                        v1=op[y[2]](op[y[0]](a, b), op[y[1]](c, d))
                        v2=op[y[2]](op[y[1]](op[y[0]](a, b), c), d)
                        if v1!=inf and int(v1)==v1>0: S[rep].append(int(v1))
                        if v2!=inf and int(v2)==v2>0: S[rep].append(int(v2))


m,a=0,0
for i in S:
    p=0
    S[i].sort()
    for j in S[i]:
        if j>p+1: break
        else: p=j
    if p>m: m,a=p,i
print(a, m)