from math import gcd

s=[]
for i in range(1, 10):
    for j in range(i+1, 10):
        for k in range(1, 10):
            n,d=10*i+j,10*j+k
            if n*k==i*d:
                s.append((n,d))

n,d=1,1
for i,j in s:
    n,d=i*n,d*j
print(d//gcd(n,d))