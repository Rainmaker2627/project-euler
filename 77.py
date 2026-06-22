L=5000
##########################################################################################

def prime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

i=3
pr=[0, 2]
dp=[[1],[0],[0,1]]
while dp[-1][-1]<L:
    if prime(i):
        pr.append(i)
    dp.append([0]*len(pr))
    for j in range(1, len(pr)):
        dp[i][j]=dp[i-pr[j]][min(j, len(dp[i-pr[j]])-1)]+dp[i][j-1]
    i+=1
print(i-1)