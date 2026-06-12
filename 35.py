N=1000000
##########################################################################################

def circ(n):
    return int(str(n)[-1]+str(n)[:-1])

S={1: False}
def p(n):
    if n in S: return S[n]
    i=2
    while i*i<=n:
        if n%i==0:
            S[n]=False
            break
        i+=1
    else:
        S[n]=True
        S[n]=p(circ(n))
    return S[n]

a=0
for i in range(1, N+1):
    if p(i):
        a+=1
        print(i)
print(a)