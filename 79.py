s=open("./input/79.txt").readlines()
##########################################################################################

s=[i.strip() for i in s]
adj,indeg=[[] for _ in range(10)],[0]*10
for i in s:
    for j in range(len(i)-1):
        indeg[int(i[j+1])]+=1
        adj[int(i[j])].append(int(i[j+1]))

pop=[]
for i in range(10):
    if indeg[i]==0 and len(adj[i])>0:
        pop.append(i)

pword=""
while len(pop)>0:
    d=pop[0]
    pword+=str(d)
    for i in adj[d]:
        indeg[i]-=1
        if indeg[i]==0:
            pop.append(i)
    pop=pop[1:]
print(pword)