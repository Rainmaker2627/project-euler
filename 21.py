N=10000
##########################################################################################

s=0
pr,lp,vp,d=[],[0]*(N+1),[0]*(N+1),[1]*(N+1)
for i in range(2, N+1):
    if lp[i]==0:
        lp[i]=i
        d[i]=1+i
        vp[i]=1
        pr.append(i)
    j=0
    while j<len(pr) and i*pr[j]<=N:
        t=i*pr[j]
        lp[t]=pr[j]
        if i%pr[j]==0:
            vp[t]=1+vp[i]
            d[t]=d[i]*(lp[t]**(vp[t]+1)-1)//(lp[t]**vp[t]-1)
        else:
            vp[t]=1
            d[t]=d[i]*(1+lp[t])
        j+=1
    if d[i]-i<i:
        s+=d[i]*(1 if d[d[i]-i]==d[i] else 0)
print(s)