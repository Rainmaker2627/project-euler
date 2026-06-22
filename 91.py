D=50
##########################################################################################

s=0
for x1 in range(D+1):
    for y1 in range(D+1):
        if (x1, y1)==(0, 0): continue
        for x2 in range(D+1):
            for y2 in range(D+1):
                if (x1, y1)==(0, 0) or (x1, y1)==(x2, y2): continue
                if x1*(x2-x1)+y1*(y2-y1)==0: s+=1
print(s+D*D)