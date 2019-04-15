def fourthBit(n):
    b=''
    if n !=0:
        while n>=1:
            if n %2==0:
                b += '0'
                n = n/2
            else:
                b += '1'
                n = (n-1)/2
    else:
        n = '0'
    
    sb = [v for v in b]
    sb = sb[::-1]
    return sb[3]

print(fourthBit(32))