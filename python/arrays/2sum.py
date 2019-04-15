def twoSum( nums, target):
    c = 1

    while c < len(nums):
        for i in range(c, len(nums)):
            if nums[c-1] + nums[i] == target:
                return [c-1, i]

        c +=1




nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
