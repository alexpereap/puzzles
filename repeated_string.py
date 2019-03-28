def repeatedString(s, n):
    total = 0
    a = 0
    l = len(s)
    for c in s:
        if c == 'a':
            a += 1
    
    print(a)


repeatedString('abcac', 10)
# abcacabcac
# abcacabcacab