d=1000
##########################################################################################

def pr(n):
    i,p=2,[]
    while i*i<=n:
        if n%i==0:
            p.append(i)
            while n%i==0:
                n//=i
        i+=1
    if n>1:
        p.append(n)
    return p

m=0
for i in range(d, -1, -1):
    p=pr(i)
    if i!=p[0]:
        continue
    d=pr(i-1)
    for j in d:
        if pow(10, (i-1)//j, i)==1:
            break
    else:
        m=i
        break
print(m)