def rotLeft(a, d):

    b = a.copy()
    for i in range(0, len(a)):
        index = (i + d) % len(a)
        b[i] = a[index]
    
    return b

print(rotLeft([1, 2, 3, 4, 5,], 4))