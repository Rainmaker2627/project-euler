N=100
##########################################################################################

def pqscfe(n):
    if n==0: return 2
    if n%3==2: return 2*(n+1)//3
    return 1

h,k,ph,pk=2,1,1,0
for i in range(1, N):
    h,k,ph,pk=h*pqscfe(i)+ph,k*pqscfe(i)+pk,h,k
print(sum([int(i) for i in str(h)]))