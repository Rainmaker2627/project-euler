s=open("./input/99.txt").readlines()
##########################################################################################
from math import log

m,r=0,-1
for i in range(len(s)):
    a,b=map(int, s[i].split(','))
    if b*log(a)>m:
        m,r=b*log(a),i
print(r+1)