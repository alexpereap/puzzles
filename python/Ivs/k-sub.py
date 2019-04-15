def kSub2(k, nums):
    t = []
    r = 0
    while len(nums) > 0:
        for v in nums:
            t.append(v)
            if sum(t) % k == 0:
                r += 1
        
        t = []
        nums = nums[::-1]
        nums.pop()
        nums = nums[::-1]
    
    return r

def kSub(k, nums):
    t = []
    r = 0
    x = 0
    while x <= len(nums):
        for i in range(x, len(nums)):
            t.append(nums[i])
            if sum(t) % k == 0:
                r += 1
        
        t = []
        x+=1
    
    return r


nums = [5, 10, 11, 9, 5]
k = 5

print(kSub(k, nums))