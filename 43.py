
p=[1,2,3,5,7,11,13,17]
def gen(d, i):
    global x, p
    if i==len(p):
        x+=int(''.join([*map(str, d)]))
        return
    m=(100*d[-2]+10*d[-1])%p[i]
    for j in range(10):
        if j in d: continue
        if (-j)%p[i]==m:
            d.append(j)
            gen(d, i+1)
            d.pop()

x=0
for i in range(1, 10):
    for j in range(0, 10):
        if i==j: continue
        gen([i, j], 0)
print(x)