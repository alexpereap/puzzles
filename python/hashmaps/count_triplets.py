from collections import Counter

def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for v in arr:
        if v in r3:
            count += r3[v]
        
        if v in r2:
            r3[v*r] += r2[v]
        
        r2[v*r] += 1

    return count


        
        



arr = [1,4,16,64]
r = 4
countTriplets(arr, r) # 1 < 4 < 16, 4 < 16 < 64, reuturn will be 2

# [1, 4, 16, 64]
# temp [i,j,k]
# 0,1
# 1 <= 4 -> t.append(0)
# 4 <= 4 -> t.append(1)
# 4 <= 16 -> t.append(2)