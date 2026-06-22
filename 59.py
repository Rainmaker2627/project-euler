s=open("./input/59.txt").readline()
t=open("./input/42.txt").readline()
##########################################################################################

msg=[*map(int, s.split(','))]

# dictionary for word identification; taken to be all caps
dict=t.split('\",\"')
dict[0]=dict[0][1:]
dict[-1]=dict[-1][:-1]
dict=set(dict)

key,hits=0,0
alph=[*range(ord('a'), ord('z')+1)]
for a in alph:
    for b in alph:
        for c in alph:
            re=""
            for i in range(len(msg)):
                if i%3==0:
                    re+=chr(msg[i]^a)
                elif i%3==1:
                    re+=chr(msg[i]^b)
                else:
                    re+=chr(msg[i]^c)
            hit=0
            for i in re.split():
                if i.capitalize() in dict:
                    hit+=1
            if hit>hits:
                hits=hit
                key=(a,b,c)

re=""
for i in range(len(msg)):
    if i%3==0:
        re+=chr(msg[i]^key[0])
    elif i%3==1:
        re+=chr(msg[i]^key[1])
    else:
        re+=chr(msg[i]^key[2])
print(sum([ord(i) for i in re]))