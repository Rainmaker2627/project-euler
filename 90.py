from itertools import combinations

s=0
S=set()
C=[0,1,2,3,4,5,6,7,8,9]
for D1 in combinations(C, 6):
    if 6 in D1:
        if 9 not in D1:
            D1=tuple([9])+D1
    elif 9 in D1: D1=tuple([6])+D1
    for D2 in combinations(C, 6):
        if 6 in D2:
            if 9 not in D2:
                D2=tuple([9])+D2
        elif 9 in D2: D2=tuple([6])+D2
        A,B=sorted(D1),sorted(D2)
        if not ((0 in D1 and 1 in D2) or (0 in D2 and 1 in D1)): continue
        if not ((0 in D1 and 4 in D2) or (0 in D2 and 4 in D1)): continue
        if not ((0 in D1 and 9 in D2) or (0 in D2 and 9 in D1)): continue
        if not ((1 in D1 and 6 in D2) or (1 in D2 and 6 in D1)): continue
        if not ((2 in D1 and 5 in D2) or (2 in D2 and 5 in D1)): continue
        if not ((3 in D1 and 6 in D2) or (3 in D2 and 6 in D1)): continue
        if not ((4 in D1 and 9 in D2) or (4 in D2 and 9 in D1)): continue
        if not ((6 in D1 and 4 in D2) or (6 in D2 and 4 in D1)): continue
        if not ((8 in D1 and 1 in D2) or (8 in D2 and 1 in D1)): continue
        s+=1
print(s//2)