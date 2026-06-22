N=1000
##########################################################################################

def fs(n):
    s,p=int(n**0.5),0
    a,d,m=s,1,0
    h,k,ph,pk=s,1,1,0
    while a!=2*s or p%2==1:
        m=d*a-m
        d=(n-m*m)//d
        a=(s+m)//d
        h,k,ph,pk=h*a+ph,k*a+pk,h,k
        p+=1
    return (ph, pk)
print(fs(12))

m,j,d=0,2,0
for n in range(2, N+1):
    if n==j*j:
        j+=1
    else:
        r=fs(n)
        assert r[0]**2-n*r[1]**2==1
        if r[0]>m: m,d=r[0],n
print(d)