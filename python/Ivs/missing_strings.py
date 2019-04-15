def missingWords(s, t):
    s = s.split()
    t = t.split()
    m = []
    for v in s:
        if v not in t and v not in m:
            m.append(v)

    print(m)

s = 'I am I alex am'
t = 'alex'

missingWords(s, t)