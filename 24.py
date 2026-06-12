N=1000000
S="0123456789"
##########################################################################################

fac=[1]
for i in range(1,len(S)):
    fac.append(fac[i-1]*i)
assert fac[-1]*len(S)>N

a=""
N-=1
for j in range(len(S)-1, -1, -1):
    d=N//fac[j]
    a+=S[d]
    S=S[:d]+S[d+1:]
    N%=fac[j]
print(a)