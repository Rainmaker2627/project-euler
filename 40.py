from math import log

def d(n):
    lo,hi=1,int(log(n, 10))+1
    while lo<hi:
        mid=(lo+hi)//2
        r=(10**mid*(9*mid-1)+1)//9
        if r<n:lo=mid+1
        else: hi=mid
    n=n-(10**(hi-1)*(9*(hi-1)-1)+1)//9-1
    n,m=n//hi,hi-n%hi-1
    if m==hi-1: return n//(10**m)+1 
    else: return n//(10**m)%10

p=1
for i in range(7):
    p*=d(10**i)
print(p)