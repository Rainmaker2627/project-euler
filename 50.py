L=1000000
##########################################################################################

S={1: False}
def pr(n):
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

L-=1
pre,c,p=[0],[0]*(L+1),[]
for i in range(2, len(c)):
    if c[i]==0:
        if pre[-1]+i>L: break
        p.append(i)
        pre.append(pre[-1]+i)
        for j in range(i*i, len(c), i):
            c[j]=1

m=0
for i in range(len(pre)):
    for j in range(1,i+1):
        if pr(pre[-j]-pre[i-j+1]):
            m=pre[-j]-pre[i-j+1]
            break
    if m>0:
        break
print(m)
            