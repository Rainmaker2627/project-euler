s=open("./input/81.txt").readlines()
##########################################################################################

s=[[int(j) for j in i.split(',')] for i in s]

N,M=len(s),len(s[0])
dp=[[0]*M for _ in range(N)]
dp[0][0]=s[0][0]
for i in range(1, M):
    dp[0][i]=dp[0][i-1]+s[0][i]
for i in range(1, N):
    dp[i][0]=dp[i-1][0]+s[i][0]
    for j in range(1, M):
        dp[i][j]=s[i][j]+min(dp[i][j-1], dp[i-1][j])
print(dp[N-1][M-1])