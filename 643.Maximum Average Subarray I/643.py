def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    nlen = len(nums)

    fin = sum(nums[0:k])
    temp = fin
    for i in range(nlen-k):
        temp = temp + nums[i+k] - nums[i]
        if temp>fin:
            fin = temp
    return fin/k

print(findMaxAverage([1,12,-5,-6,50,3], 4))
