import math
def sockMerchant(n, ar):
    total_pairs = 0

    if( n < 2 ):
        return 0

    for idx, col in enumerate(ar):
        pairs = 0
        ar3 = []

        if idx == 0:
            ar2 = ar.copy()

        for idx2, col2 in enumerate(ar2):
            if col == col2:
                pairs = pairs + 1
            else:
                ar3.append(col2)

        ar2 = ar3.copy()
        total_pairs = total_pairs + math.floor(pairs/2)

    return total_pairs

    
r = sockMerchant(1, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])
print(r)