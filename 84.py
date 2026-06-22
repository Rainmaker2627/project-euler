D=6
##########################################################################################
from fractions import Fraction
from math import lcm

N=40
GO,TJAIL,JAIL,G2J=0,40,10,30
CH,CC={7,22,36},{2,17,33}
NR,NU={7:15, 22:25, 36:5},{7:12, 22:28, 36: 12}
def rules(p):
    t=[Fraction(0)]*(N+1)
    for i in range(N):
        if p[i]==0: continue
        prob=p[i]*Fraction(1, 16)
        if i == G2J:
            t[TJAIL]+=16*prob
        elif i in CC:
            t[GO]+=prob
            t[TJAIL]+=prob
            t[i]+=14*prob
        elif i in CH:
            t[i]+=6*prob
            t[GO]+=prob
            t[TJAIL]+=prob
            t[11]+=prob  # C1
            t[24]+=prob  # E3
            t[39]+=prob  # H2
            t[5]+=prob   # R1
            t[NR[i]]+=2*prob
            t[NU[i]]+=prob
            if i-3 in CC:
                t[GO]+=prob/16
                t[TJAIL]+=prob/16
                t[i-3]+=14*prob/16
            else:
                t[i-3]+=prob            
        else:
            t[i]+=16*prob
    return t

ndb=[Fraction(0)]+[Fraction(min(i, 2*D-i)-(i%2), D**2) for i in range(2*D)]
db=[Fraction(0)]+[Fraction(i%2, D**2) for i in range(2*D)]
def roll(p):
    pg,pb=[Fraction(0)]*N,[Fraction(0)]*N
    for n in range(len(db)):
        if db[n]>0 or ndb[n]>0:
            sft=p[-(n%len(p)):]+p[:-(n%len(p))]
            for i in range(N):
                pg[i]+=sft[i]*db[n]
                pb[i]+=sft[i]*ndb[n]
    good,bad=rules(pg),rules(pb)
    bad[JAIL]+=good[TJAIL]+bad[TJAIL]
    return bad[:N],good[:N]

T,V=[],[]
norm = 1
for i in range(N):
    p = [Fraction(0)]*N; p[i] += 1
    d1, a1 = roll(p)
    d2, a2 = roll(a1)
    d3, d4 = roll(a2)
    v = [Fraction(0)] * N
    for j in range(N):
        v[j]=d1[j]+a1[j]+d2[j]+a2[j]+d3[j]
    v[JAIL]+=sum(d4)
    V.append(v)

    for j in range(N):
        p[j]+=d1[j]+d2[j]+d3[j]
    p[JAIL]+=sum(d4)
    p[i]-=1
    T.append(p)
    
    for j in range(N):
        if p[j]==0: continue
        norm=lcm(p[j].denominator, norm)

def bred(P):
    n=len(P)
    prev_pivot=1
    for k in range(n):
        for i in range(k+1, n):
            for j in range(k+1, n):
                # bareiss update formula
                P[i][j]=(P[i][j]*P[k][k]-P[i][k]*P[k][j])//prev_pivot
            P[i][k]=0
        prev_pivot=P[k][k]
    return P

P=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        P[j][i]=(T[i][j]*norm).numerator
        if i==j: P[i][j]-=norm
P=bred(P)

end=[Fraction(0)]*N
end[N-1]=Fraction(1)
for i in range(N-2, -1, -1):
    current_sum=sum((P[i][j]*end[j] for j in range(i+1, N)), Fraction(0, 1))
    end[i]=-current_sum/P[i][i]
total = sum(end)
end=[val/total for val in end]

vis=[Fraction(0)]*N
for i in range(N):
    for j in range(N):
        vis[j]+=end[i]*V[i][j]
total=sum(vis)
vis=[val/total for val in vis]

res=sorted([(vis[i], i) for i in range(N)])
for i in res[::-1]:
    a,b=i[0].as_integer_ratio()
    print(f"{i[1]:02d} {a/b:.7f}")