def two_pointers(arr, x):
    # left pointer
    i = 0
    # right pointer
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == x:
            return [arr[i], arr[j]]
        
        # If sum of elements at current 
        # pointers is less, we move towards 
        # higher values by doing i++ 
        elif arr[i] + arr[j] < x:
            i += 1
        # If sum of elements at current 
        # pointers is more, we move towards 
        # lower values by doing j-- 
        else:
            j -= 1

    return False

        


arr = [10, 20, 35, 50, 75, 80]
print(two_pointers(arr, 70))