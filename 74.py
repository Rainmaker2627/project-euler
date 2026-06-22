N=1000000
##########################################################################################

fac=[1]
for i in range(1,10):
    fac.append(fac[-1]*i)

dp={}
fdsum=lambda n: sum([fac[int(i)] for i in str(n)])
def go(n, k):
    if n not in dp: dp[n]=0
    if dp[n]<0:
        dp[n]+=k
        return k
    elif dp[n]==0:
        dp[n]=-k
        dp[n]+=go(fdsum(n), k+1)
        return dp[n]+k
    return k+dp[n]

s=0
for i in range(1, N):
    if go(i, 1)-1==60:
        s+=1
print(s)