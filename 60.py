L=20000000
S={1: False}
def p(n):
    if n in S: return S[n]
    elif n<L: return False
    i=2
    while i*i<=n:
        if n%i==0:
            S[n]=False
            break
        i+=1
    else:
        S[n]=True
    return S[n]


c,pr=[0]*(L+1),[]
for i in range(2, len(c)):
    if c[i]==0:
        pr.append(i)
        S[i]=True
        for j in range(i*i, len(c), i):
            c[j]=1

M=1100
adj=[set() for _ in range(M)]
for i in range(1, M):
    for j in range(i+1, M):
        if p(int(str(pr[i])+str(pr[j]))) and p(int(str(pr[j])+str(pr[i]))):
            adj[i].add(j)

m=L*5
for i in range(1, M):
    for j in adj[i]:
        ij=adj[i].intersection(adj[j])
        for k in ij:
            ijk=adj[k].intersection(ij)
            for l in ijk:
                ijkl=adj[l].intersection(ijk)
                if len(ijkl)>0:
                    m=min(m, pr[i]+pr[j]+pr[k]+pr[l]+pr[min(ijkl)])
print(m)