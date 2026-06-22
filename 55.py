N=10000
##########################################################################################

def pal(n):
    s=str(n)
    for i in range(len(s)//2):
        if s[-i-1]!=s[i]:
            return False
    return True

a=0
ra=lambda n: int(str(n))+int(str(n)[::-1])
for i in range(1, N+1):
    s,t=50,ra(i)
    while s>0 and not pal(t):
        t=ra(t)
        s-=1
    if s==0:
        a+=1
print(a)