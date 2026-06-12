def palindrome(s):
    for i in range(len(s)):
        if s[i]!=s[-1-i]:
            return False
    return True

m=0
for i in range(999, -1, -1):
    for j in range(999, -1, -1):
        if i*j<=m: break
        if palindrome(str(i*j)):
            m=i*j
print(m)