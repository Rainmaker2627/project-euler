s=open("./input/18.txt").readlines()
##########################################################################################

a=[[int(j) for j in i.split()] for i in s]
dp=[[0]*(i+3) for i in range(len(a))]
dp[0][1]=a[0][0]
for i in range(1, len(a)):
    for j in range(1, i+2):
        dp[i][j]=a[i][j-1]
        dp[i][j]+=max(dp[i-1][j-1], dp[i-1][j])

m=dp[-1][1]
for i in dp[-1][1:-1]:
    m=max(m, i)
print(m)