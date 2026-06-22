N=2000000
##########################################################################################

i=1
fac=[1]
while i*(i-1)//2 < N:
    fac.append(fac[-1]*i)
    i+=1

def comb(n, k):
    return fac[n]//(fac[k]*fac[n-k])

# nC2 * mC2
n=i-1
ans=comb(n, 2)
d,r=abs(N-ans),(n,2)
for m in range(3, i-1):
    t=comb(m, 2)
    while comb(n, 2)*t>N:
        n-=1
        v=abs(N-comb(n, 2)*comb(m, 2))
        if v<=d:
            r=(n-1,m-1)
            d=v
    if n<m: break
print(r[1]*r[0])