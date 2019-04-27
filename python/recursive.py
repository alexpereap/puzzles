def fact(n):
    if n == 0:
        return 1
    else:
        f = fact(n-1)
        r =  n * f
        return r

print(fact(6))