s=open("./input/54.txt").readlines()
##########################################################################################

m={"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
def rate(cards):
    ranks=sorted([m[card[0]] for card in cards])
    suits=[card[1] for card in cards]
    counts={ranks.count(i) for i in range(1, 15)}

    flush = ( len(set(suits))==1 )
    straight = ( len(set(ranks))==5 and ranks[4]==4+ranks[0] )

    if flush and straight:
        return ((8, ranks[4]), (8, ranks[3]), (8, ranks[2]), (8, ranks[1]), (8, ranks[0]))
    if 4 in counts:
        four = ranks[0] if ranks[0]==ranks[1] else ranks[-1]
        one = ranks[0]+ranks[-1]-four
        return ((7, four), (0, one))
    if 3 in counts and 2 in counts:
        three = ranks[0] if ranks[0]==ranks[2] else ranks[-1]
        two = ranks[0]+ranks[-1]-three
        return ((6, three), (6, two))
    if flush:
        return ((5, ranks[4]), (5, ranks[3]), (5, ranks[2]), (5, ranks[1]), (5, ranks[0]))
    if straight:
        return ((4, ranks[4]), (4, ranks[3]), (4, ranks[2]), (4, ranks[1]), (4, ranks[0]))
    if 3 in counts:
        three,ones=0,[]
        for i in ranks:
            if ranks.count(i)==3:
                three=i
            else:
                ones.append(i)
        return ((3, three), (0, ones[1]), (0, ones[0]))
    if 2 in counts:
        twos,ones=[],[]
        for i in ranks:
            if ranks.count(i)==2:
                if i not in twos:
                    twos.append(i)
            else:
                ones.append(i)
        if len(twos)==2:
            return ((2, twos[1]), (2, twos[0]), (0, ones[0]))
        else:
            return ((1, twos[0]), (0, ones[2]), (0, ones[1]), (0, ones[0]))
    return ((0, ranks[4]), (0, ranks[3]), (0, ranks[2]), (0, ranks[1]), (0, ranks[0]))

def winner(s):
    t=s.split()
    p1=rate(t[:5])
    p2=rate(t[5:])
    if p1==p2:
        return 0
    return 2 if p1<p2 else 1

a=0
for i in s:
    a+=(1 if winner(i)==1 else 0)
print(a)