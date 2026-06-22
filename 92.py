L=10000000
##########################################################################################

dp=[0]*(L+1)
dp[1]=1; dp[89]=89
T=lambda n: 0 if n==0 else (n%10)**2+T(n//10)
for i in range(1, L+1):
    if dp[i]>0: continue
    s=[i]
    while dp[s[-1]]==0:
        s.append(T(s[-1]))
    for i in s: dp[i]=dp[s[-1]]
print(dp.count(89))