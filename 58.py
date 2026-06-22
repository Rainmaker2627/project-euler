L=10
##########################################################################################

def pr(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return 0
        i+=1
    return 1

n,p=1,3
s=[1,3,5,7,9]
d=lambda n: (2*n+1)**2
while L*p>=len(s):
    n+=1
    t=d(n)
    s.extend([t-6*n, t-4*n, t-2*n, t])
    p+=pr(t)+pr(t-2*n)+pr(t-4*n)+pr(t-6*n)
print(2*n+1)