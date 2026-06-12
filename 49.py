from itertools import permutations

S={1: False}
def p(n):
    if n in S: return S[n]
    i=2
    while i*i<=n:
        if n%i==0:
            S[n]=False
            break
        i+=1
    else:
        S[n]=True
    return S[n]

for i in range(1, 10):
    for j in range(i, 10):
        for k in range(j, 10):
            for l in range(k, 10):
                n=l+10*(k+10*(j+10*i))
                T=set([int(''.join(i)) for i in permutations(str(n))])
                for a in T:
                    if not p(a): continue
                    for b in T:
                        if not p(b): continue
                        if (a>b) and (2*a-b in T) and p(2*a-b):
                            print(str(b)+str(a)+str(2*a-b))
