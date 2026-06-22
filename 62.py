N=6
##########################################################################################

S={}
n,m,b=0,0,0
while True:
    v=''.join(sorted(str(n**3)))
    if b>0 and len(v)>b: break
    if v in S:
        p=S[v]
        if p[1]==N-1:
            m=p[0] if m==0 else min(m, p[0])
            if m==p[0]: b=len(v)
        else:
            S[v]=(p[0], p[1]+1)
    else:
        S[v]=(n, 1)
    n+=1
print(m**3)