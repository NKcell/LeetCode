def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    for i,element in enumerate(nums):
        if element >= target:
            return i
    return len(nums)

print(searchInsert([1,3,5,6], 0))