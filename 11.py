s=open("./input/11.txt").readlines()
##########################################################################################

m=0
a=[[int(j) for j in i.split()] for i in s]
for i in range(len(a)): # rows
    for j in range(len(a[0])-4):
        m=max(m, a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3])
for i in range(len(a)-4): # cols
    for j in range(len(a[0])):
        m=max(m, a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j])
for i in range(len(a)-4): # diag down
    for j in range(len(a[0])-4):
        m=max(m, a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3])
for i in range(len(a)-4): # diag up
    for j in range(3,len(a[0])):
        m=max(m, a[i][j]*a[i+1][j-1]*a[i+2][j-2]*a[i+3][j-3])
print(m)