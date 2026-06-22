N=10000
##########################################################################################

def scf(n):
    s,p=int(n**0.5),0
    a,d,m=s,1,0
    while a!=2*s:
        m=d*a-m
        d=(n-m*m)//d
        a=(s+m)//d
        p+=1
    return p

s,i=0,2
for j in range(2, N+1):
    if i*i==j:
        i+=1
        continue
    if scf(j)%2==1:
        s+=1
print(s)