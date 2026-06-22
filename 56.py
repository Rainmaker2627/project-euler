A=100
B=100
##########################################################################################

def dsum(n):
    if n==0: return 0
    return n%10+dsum(n//10)

m=0
for a in range(1, A):
    for b in range(1, B):
        m=max(m, dsum(a**b))
print(m)