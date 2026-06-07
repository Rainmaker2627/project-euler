s=open("./code/input.txt").readline()
N=13
##################

p,a=[0]*N,[int(i) for i in s]
for i in range(N):
    if i>0: p[i]=p[i-1]
    p[i]*=a[i]

m=p[-1]
for i in range(len(s)):
    p=[a[i]]+p
    p.pop()
    for j in range(1, N):
        p[j]*=a[i]
    m=max(m, p[-1])
print(m)