N=1000000
##########################################################################################

S={1:0}
def csl(n):
    if n not in S:
        S[n]=1+csl(3*n+1 if n%2==1 else n//2)
    return S[n]

m,a=0,0
for i in range(1, N):
    if csl(i)>m:
        m=csl(i)
        a=i
print(a)