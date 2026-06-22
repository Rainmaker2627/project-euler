s=open("./input/89.txt").readlines()
##########################################################################################

def toint(s):
    n,i=0,len(s)-1
    while i>=0:
        if s[i]=='M':
            if i>0 and s[i-1]=='C': n+=900; i-=1
            else: n+=1000
        elif s[i]=='D':
            if i>0 and s[i-1]=='C': n+=400; i-=1
            else: n+=500
        elif s[i]=='C':
            if i>0 and s[i-1]=='X': n+=90; i-=1
            else: n+=100
        elif s[i]=='L':
            if i>0 and s[i-1]=='X': n+=40; i-=1
            else: n+=50
        elif s[i]=='X':
            if i>0 and s[i-1]=='I': n+=9; i-=1
            else: n+=10
        elif s[i]=='V':
            if i>0 and s[i-1]=='I': n+=4; i-=1
            else: n+=5
        elif s[i]=='I':
            n+=1
        i-=1
    return n

def torom(n):
    s=""
    while n>0:
        if n>=1000:
            s+="M"; n-=1000
        elif n>=900:
            s+="CM"; n-=900
        elif n>=500:
            s+="D"; n-=500
        elif n>=400:
            s+="CD"; n-=400
        elif n>=100:
            s+="C"; n-=100
        elif n>=90:
            s+="XC"; n-=90
        elif n>=50:
            s+="L"; n-=50
        elif n>=40:
            s+="XL"; n-=40
        elif n>=10:
            s+="X"; n-=10
        elif n>=9:
            s+="IX"; n-=9
        elif n>=5:
            s+="V"; n-=5
        elif n>=4:
            s+="IV"; n-=4
        else:
            s+="I"; n-=1
    return s

a=0
s=[i.strip() for i in s]
for i in s:
    a+=len(i)-len(torom(toint(i)))
print(a)