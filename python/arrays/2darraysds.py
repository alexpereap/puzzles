def hourglassSum(arr):
    total = None

    left = 0
    right = 3
    middle = 1
    row = 0

    for i in range(1,17):
        initialSubset = arr[row][left:right]
        initialSubset.append(arr[row+1][middle])
        initialSubset = initialSubset + arr[row+2][left:right]

        temp_total = sum(initialSubset)

        if total is None:
            total = temp_total
        elif temp_total > total:
            total = temp_total
        
        left += 1
        right += 1
        middle += 1

        if i % 4 == 0:
            row += 1
            left = 0
            right = 3
            middle = 1

    return total        

array = [
    [1 ,1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

print(hourglassSum(array))