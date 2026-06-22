P=[
    lambda n: n*(n+1)//2,
    lambda n: n*n,
    lambda n: n*(3*n-1)//2,
    lambda n: n*(2*n-1),
    lambda n: n*(5*n-3)//2,
    lambda n: n*(3*n-2)
]

n=1
T=[]
S=[{} for _ in range(6)]
while P[0](n)<10000:
    for i in range(6):
        t=P[i](n)
        if 1000<t<10000:
            if i==0: T.append(t)
            else:    
                if (t//100)%100 in S[i]:
                    S[i][(t//100)%100].append(t)
                else: S[i][(t//100)%100]=[t]
    n+=1

def gen(used, go, start):
    if len(used)==6:
        if go%100==start:
            return (True, go)
        return (False, "")
    for i in range(6):
        if i in used: continue
        used.append(i)
        if go%100 in S[i]:
            for j in S[i][go%100]:
                res=gen(used, 100*go+(j%100), start)
                if res[0]:
                    return res
        used.pop()
    return (False, "")

for i in T:
    res=gen([0], i, i//100)
    if res[0]:
        s,t=0,res[1]
        while t>1000:
            s+=t%10000
            t//=100
        print(s)
        break