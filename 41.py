
fac=[1]
for i in range(1,8):
    fac.append(fac[i-1]*i)

T={1: False}
def p(n):
    if n in T: return T[n]
    i=2
    while i*i<=n:
        if n%i==0:
            T[n]=False
            break
        i+=1
    else:
        T[n]=True
    return T[n]

def perm(S, N):
    a=0
    for j in range(len(S)-1, -1, -1):
        d=N//fac[j]
        a=10*a+int(S[d])
        S=S[:d]+S[d+1:]
        N%=fac[j]
    return a

m=0
for d in range(7, 1, -3):
    N,S=fac[d],''.join([*map(str, [*range(1,d+1)])])[::-1]
    for i in range(0, N):
        a=perm(S, i)
        if p(a):
            m=a
            break
    if m>0: break
print(m)