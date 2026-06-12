
S={}
def p(n):
    if n<0: return False
    if n in S: return S[n]
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

m,r=0,0
for b in range(0, 1001):
    if not p(b):
        continue
    for a in range(-1000, 1000):
        T=lambda n: n*(n+a)+b
        for i in range(1, b):
            if not p(T(i)):
                break
            if i>m:
                m,r=i,a*b
print(r)