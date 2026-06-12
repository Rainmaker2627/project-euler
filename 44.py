from math import isqrt

p=lambda n: n*(3*n-1)//2
rp=lambda x: (1+isqrt(1+24*x))//6

d=1
while True:
    x,pd=(d-1)%3+1,2*p(d)
    while x<=d:
        if (2*pd)%x==0:
            y=pd//x
            if y%3==2:
                kpj=(1+pd//x)//3
                if kpj%2==x%2:
                    k,j=(kpj+x)//2,(kpj-x)//2
                    ps=p(k)+p(j)
                    if j>0 and p(rp(ps))==ps:
                        print(p(k)-p(j))
                        quit()
        x+=3
    d=d+1