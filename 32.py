
rel=[[0],[],[],[],[]]
for i in range(1, 10000):
    t=str(i)
    s=set(j for j in t)
    if '0' not in s and len(t)==len(s):
        rel[len(s)].append(i)

a=set()
for i in rel[1]:
    for j in rel[4]:
        if i*j>9876: break
        t=str(i)+str(j)+str(i*j)
        s=set(k for k in t)
        if len(s)==len(t)==9 and '0' not in s:
            a.add(i*j)
for i in rel[2]:
    for j in rel[3]:
        if i*j>9876: break
        t=str(i)+str(j)+str(i*j)
        s=set(k for k in t)
        if len(s)==len(t)==9 and '0' not in s:
            a.add(i*j)
print(sum(a))