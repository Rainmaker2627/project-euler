N=1000000
##########################################################################################

def palindrome(s):
    for i in range(len(s)):
        if s[i]!=s[-1-i]:
            return False
    return True

s=0
for i in range(1, N):
    if palindrome(str(i)) and palindrome(bin(i)[2:]):
        s+=i
        print(str(i), bin(i)[2:])
print(s)