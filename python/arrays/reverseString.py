def reverseString(s):
    r = ''
    for v in s:
        r = v + r

    print(r)

s = 'hola'
reverseString(s)