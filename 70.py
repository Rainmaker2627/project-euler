N=10000000
##########################################################################################

s=2
lp,pr=[0]*(N+1),[]
phi=[0]*(N+1)
phi[1]=1
for i in range(2, N+1):
    if lp[i]==0:
        lp[i]=i
        phi[i]=i-1
        pr.append(i)
    j=0
    while j<len(pr) and i*pr[j]<=N:
        lp[i*pr[j]]=pr[j]
        if i%pr[j]==0:
            phi[i*pr[j]]=phi[i]*pr[j]
        else:
            phi[i*pr[j]]=phi[i]*(pr[j]-1)
        if pr[j]==lp[i]:
            break
        j+=1
    if sorted(str(phi[i]))==sorted(str(i)):
        if i*phi[s]<s*phi[i]:
            s=i
print(s)