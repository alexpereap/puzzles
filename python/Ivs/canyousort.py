def customSort(arr):
    repeated_subset = []
    unique_subset = []
    log_subset = []

    for v in arr:
        if v not in log_subset:
            unique_subset.append(v)
            log_subset.append(v)
        else:
            if v in repeated_subset:
                repeated_subset.append(v)
            else:
                repeated_subset.append(v)
                repeated_subset.append(v)
            if v in unique_subset:
                i = unique_subset.index(v)
                del(unique_subset[i])

    unique_subset.sort()
    repeated_subset = sorted(repeated_subset,key=repeated_subset.count)

    print(unique_subset)
    print(repeated_subset)
    

    # r = unique_subset+repeated_subset
    # for x in r:
    #     print(x)


arr = [8,5,5,5,7,5,1,1,1,4,4,0]
print(customSort(arr))