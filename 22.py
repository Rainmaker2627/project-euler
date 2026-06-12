s=open("./input/22.txt").readline()
##########################################################################################

x=0
a=s.split('\",\"')
a[0]=a[0][1:]
a[-1]=a[-1][:-1]
a.sort()
t=lambda c: ord(c)-ord('A')+1
for i in range(len(a)):
    x+=(i+1)*sum(map(t, [*a[i]]))
print(x)