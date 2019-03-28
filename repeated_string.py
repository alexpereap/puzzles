def repeatedString(s,n):
    l = len(s)
    q, r = divmod(n, l)
    a = 0
    # get number of a
    for c in s:
        if c == 'a':
            a+=1

    total = a*q

    for x in range(0, r):
        if( s[x] == 'a' ):
            total += 1

    return total
    

repeatedString('a', 100000000)
#abcac abcac abc
