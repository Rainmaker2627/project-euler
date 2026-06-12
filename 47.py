
def dpf(n):
    i,d=3,(n+1)%2
    while i*i<=n:
        if n%i==0:
            d+=1
            while n%i==0:
                n//=i
        i+=2
    if n:
        d+=1
    return d

n,c=2*3*5*17+1,1
while c<4:
    if dpf(n)==4:
        c+=1
    else:
        c=0
    n+=1
print(n-4)