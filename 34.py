
f=[1]
for i in range(1, 10):
    f.append(f[-1]*i)

s=0
for i in range(1, 2310000):
    if i==sum([f[int(j)] for j in str(i)]):
        s+=i
print(s-3)