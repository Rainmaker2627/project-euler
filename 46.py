from math import isqrt

L=40000
n,p=[1]*L,[]
S=set()
for i in range(2, L):
    if n[i]:
        p.append(i)
        S.add(i)
        for j in range(i*i, L, i):
            n[j]=False

for i in range(9, L, 2):
    if i in p: continue
    fail=False
    for j in p:
        if i-j<0:
            fail=True
            break
        sqrt=isqrt((i-j)//2)
        if sqrt**2==(i-j)//2:
            break
    if fail:
        print(i)
        break