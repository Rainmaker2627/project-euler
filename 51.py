
L=1000000
c,p,S=[0]*(L+1),[],{}
for i in range(2, len(c)):
    if c[i]==0:
        p.append(i)
        S[i]=1
        for j in range(i*i, len(c), i):
            c[j]=1

good=""
for i in p:
    s=str(i)
    for d in range(0, 10):
        c=s.count(str(d))
        if c==0: continue
        for j in range(1,2**c):
            ts,x="",c
            for t in range(len(s)):
                if s[t]==str(d):
                    x-=1
                    if (j&(1<<x))>0: ts+='#'
                    else: ts+=str(d)
                else: ts+=s[t]
            if ts in S:
                S[ts]+=1
                if S[ts]==8:
                    good=ts
                    break
            else:
                S[ts]=1
        if good!="": break
    if good!="": break

for d in range(1, 10):
    if S[int(good.replace('#', str(d)))]==1 or d==1:
        print(good.replace('#', str(d)))
        break