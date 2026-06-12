
def gen(n):
    global m
    s,i=str(n),2
    while len(s)<9:
        i,s=i+1,s+str(i*n)
    if len(set(j for j in s))==len(s)==9 and '0' not in s:
        m=max(int(s), m)
    if i>3:
        for j in range(1, 10):
            gen(10*n+j)

m=0
for i in range(1, 10):
    gen(i)
print(m)