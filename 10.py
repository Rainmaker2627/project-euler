N=2000000
##########################################################################################

r=int(N**0.5)
V=[N//i for i in range(1, r+1)]+[*range(1, N//r)][::-1]
S={i: i*(i+1)//2 for i in V}
for p in range(2, r+1):
    if S[p]>S[p-1]:
        x=S[p-1]
        for v in V:
            if v<p*p:
                break
            S[v]-=p*(S[v//p]-x)
print(S[N]-1)