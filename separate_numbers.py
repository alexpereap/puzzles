def beautyNum(s):
    if len(s) == 1 or s[0] == '0' or len(s) < 3:
       print('No')
       return

    for idx, val in enumerate(s):
        print(val)

    



beautyNum('7')
beautyNum('010203')
beautyNum('13')
beautyNum('10203')