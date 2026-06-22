S={i:{} for i in range(28)}
for i in range(1, 11):
    for j in range(1, 10):
        if i==j: continue
        for k in range(1, 10):
            if i==k or j==k: continue
            if j not in S[i+j+k]: S[i+j+k][j]=[]
            S[i+j+k][j].append([i,j,k])

X=[]
cur=[]
def go(sum, num):
    global cur
    if num==4:
        for i in S[sum][cur[-1]]:
            if i[0] in cur or i[2]!=cur[1]: continue
            cur+=i
            X.append(cur)
            cur=cur[:-3]
    for i in S[sum][cur[-1]]: # iterate: a+b+c=sum and b=cur[-1]
        if i[0] in cur or i[2] in cur: continue
        cur+=i
        go(sum, num+1)
        cur=cur[:-3]

for k in range(6, 28): #iterate sum
    for i in S[k]: #iterate middle number
        for j in S[k][i]:
            cur=[j[0], j[1], j[2]]
            go(k, 1)

A=0
for V in X:
    T=[[V[i], V[i+1], V[i+2]] for i in range(0,len(V),3)]
    m=min([V[i] for i in range(0,len(V),3)])
    while T[0][0]!=m:
        T=T[1:]+[T[0]]
    s=""
    for i in T:
        for j in i:
            s+=str(j)
    A=max(A, int(s))
print(A)