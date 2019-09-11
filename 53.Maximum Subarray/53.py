def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxsum = max(nums)
    count = 0
    for i in range(len(nums)):
        sum = 0
        if nums[i] > 0:
            for j in nums[i:]:
                sum += j
                if sum < 0:
                    break
                maxsum = max(sum, maxsum)
    return  maxsum

print(maxSubArray( [-2,1,-3,4,-1,2,1,-5,4]))