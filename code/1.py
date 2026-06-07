n=1000
##################

n-=1
T=lambda n: n*(n+1)//2
ans=3*T(n//3)+5*T(n//5)-15*T(n//15)
print(ans)