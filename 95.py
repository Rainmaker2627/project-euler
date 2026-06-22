N=1000000
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

a,r=0,0
vis=[0]*(N+1)
go=lambda n: d[n]-n
for i in range(1, N+1):
    if vis[i]: continue
    t=i
    while t<=N and vis[t]==0:
        vis[t]=i
        t=go(t)
    if t>N or vis[t]<i: continue
    s,m,l=go(t),t,1
    while s!=t:
        m,s,l=min(m, s),go(s),l+1
    if l>r: r,a=l,m
print(a, r)