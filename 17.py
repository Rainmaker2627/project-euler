
def word100(n):
    digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    hundred_filler = " hundred "
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    s=""
    if (n//100)%10>0:
        s+=digit[(n//100)%10]+hundred_filler
        if n%100>0:
            s+="and "
    if (n//10)%10<=1:
        s+=(digit+teens)[n%100]
    else:
        s+=tens[(n//10)%10]
        if n%10>0:
            s+='-'+digit[n%10]
    return s

def word(n):
    large_filler = ["", "thousand", "million", "billion"]
    assert n<1000**len(large_filler)

    s=word100(n%1000)
    if n<1000: return s
    if 0<n%1000<10: s="and "+s

    i=1
    n//=1000
    while n:
        if n%1000!=0:
            s=word100(n%1000)+" "+large_filler[i]+" "+s
        n//=1000
        i+=1
    return s

a=0
for n in range(1, 1001):
    s=word(n)
    s=s.replace(" ", "").replace("-", "")
    a+=len(s)
print(a)