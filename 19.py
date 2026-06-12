c,d=0,1
for y in range(1900, 2000+1):
    m=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (y%4==0 and y%100!=0) or (y%400==0):
        m[1]+=1
    for i in range(len(m)):
        if d%7==0 and y!=1900:
            c+=1
        d=(d+m[i])%7
print(c)