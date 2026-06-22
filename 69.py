L=1000000
##########################################################################################

def pr(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

i,p=2,1
while p*i<L:
    if pr(i):
        p*=i
    i+=1

print(p)