N=100
L=1000000
##########################################################################################

fac=[1]
for i in range(1, N+1):
    fac.append(fac[-1]*i)

s=0
comb=lambda n,m: fac[n]//(fac[n-m]*fac[m])
for n in range(1, N+1):
    for m in range(0, N+1):
        if comb(n,m)>L:
            s+=1
print(s)
