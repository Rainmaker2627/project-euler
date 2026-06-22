a,b=1,3
c,d=1,2
L=12000
##########################################################################################

lp,pr=[0]*(L+1),[]
mu,mert=[1]*(L+1),[0]*(L+1)
mert[1]=1
for i in range(2, L+1):
    if lp[i]==0:
        lp[i]=i
        mu[i]=-1
        pr.append(i)
    j=0
    while j<len(pr) and i*pr[j]<=L:
        lp[i*pr[j]]=pr[j]
        if i%pr[j]==0:
            mu[i*pr[j]]=0
        else:
            mu[i*pr[j]]=-mu[i]
        if pr[j]==lp[i]:
            break
        j+=1
    mert[i]=mert[i-1]+mu[i]

hi,lo=-1 if d<=L else 0,0
for i in range(1, L+1):
    hi+=(c*i//d)*mert[L//i]
    lo+=(a*i//b)*mert[L//i]
print(hi-lo)