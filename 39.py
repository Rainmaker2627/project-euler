N=1000
##########################################################################################

def triples(s):
    p=[]
    if s%2==1: return p
    for a in range(s//2+1, s-int(s/(2+2**0.5))):
        if s**2//2%a==0:
            p.append([s-s**2//(2*a), s-a, s**2//(2*a)-s+a])
    return p

m,a=0,0
for i in range(1, N):
    p=triples(i)
    if len(p)>m:
        m,a=len(p),i
print(a)