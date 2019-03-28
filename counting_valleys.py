def countingValleys(n, s):
    if not(2 <= n and n <= 10 ** 6):
        return 0
    
    level = 0
    in_valley = False
    entered_valley = 0
    for direction in s:

        if direction == 'U':
            level = level + 1
        elif direction == 'D':
            level = level - 1
        else:
            return 0

        if not in_valley and level < 0:
            in_valley = True
            entered_valley = entered_valley + 1
        elif in_valley and level == 0:
            in_valley = False

    print(entered_valley)

countingValleys(8, 'UDDDUDUU')
countingValleys(8, 'UDDDUDUUUUDDDUUUDDDDUDUU')
