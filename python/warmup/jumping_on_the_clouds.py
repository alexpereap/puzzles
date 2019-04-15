def jumpingOnClouds(c):
    jumps, i = 0, 0
    while i < len(c)-1:
        # if 2 cloud jumps
        if i+2 < len(c) and c[i+2] != 1:
            i += 1
        jumps += 1
        i += 1
    print(jumps)

jumpingOnClouds([0, 0, 0, 1, 0, 0]) # 3
jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) # 4
jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]) # 3
jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0]) #6
jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0 ,0])
