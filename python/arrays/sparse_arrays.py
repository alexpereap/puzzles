def matchingStrings(strings, queries):
    r = []
    for q in queries:
        m = 0
        for s in strings:
            if s == q:
                m += 1
        r.append(m)
    
    return r



strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb', 'ab']

print(matchingStrings(strings, queries))