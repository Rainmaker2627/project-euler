
def ds(n):
    d=[int(i) for i in str(n)]
    return sum(map(lambda n: n**5, d))

s=0
L=10**6
for i in range(2, L):
    if ds(i)==i:
        print(i)
        s+=i
print(s)