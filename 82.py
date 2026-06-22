s=open("./input/82.txt").readlines()
##########################################################################################
import heapq

s=[[int(j) for j in i.split(',')] for i in s]

N,M=len(s),len(s[0])
dp=[[0]*M for _ in range(N)]
h=[(0, (i, 0)) for i in range(N)]
while len(h)>0:
    w,p=heapq.heappop(h)
    i,j=p
    if dp[i][j]==0:
        dp[i][j]=s[i][j]+w
        if j==M-1:
            break
        if i>0 and dp[i-1][j]==0:
            heapq.heappush(h, (dp[i][j], (i-1, j)))
        if i<N-1 and dp[i+1][j]==0:
            heapq.heappush(h, (dp[i][j], (i+1, j)))
        if dp[i][j+1]==0:
            heapq.heappush(h, (dp[i][j], (i, j+1)))
print(dp[i][j])