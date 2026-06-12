
S={1: False, 2: True, 3: True, 5: True, 7: True, 9: False}
def p(n):
    if n in S: return S[n]
    i=2
    while i*i<=n:
        if n%i==0:
            S[n]=False
            break
        i+=1
    else:
        S[n]=True
    return S[n]

def gen_right(n):
    global a
    if p(n):
        if check_left(n):
            a+=n
        for d in [1, 3, 7, 9]:
            gen_right(10*n+d)

T={1: False, 2: True, 3: True, 5: True, 7: True}
def check_left(n):
    if n in T: return T[n]
    T[n]=p(n) and check_left(int(str(n)[1:]))
    return T[n]

a=0
for d in [2,3,5,7]:
    gen_right(d)
print(a-17)
