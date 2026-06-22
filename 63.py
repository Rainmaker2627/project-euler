
k,n,s=1,1,0
while k<10:
    while k**n < 10**(n-1):
        k+=1
    n+=1
    s+=10-k
print(s)
