p=100
N=100
##########################################################################################
from math import isqrt

L=10**p
def sqrt(D):
    s=round(D**0.5)
    a,b,e=s,1,2
    while e<L:
        a,b=a**2+D*b**2,2*a*b
        e=s*e**2
    return a, b

def dec(a, b, n):
    s=str(a//b)+'.'
    a=a%b
    for _ in range(n):
        a=a*10
        s+=str(a//b)
        a%=b
    return s

j,x=1,0
for i in range(1, N+1):
    if j*j==i:
        j+=1
    else:
        a,b=sqrt(i)
        s=dec(a,b,p)
        s=s.replace('.','')
        x+=sum(int(i) for i in s[:p])
print(x)