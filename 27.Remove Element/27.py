def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    while val in nums:
        nums.remove(val)
    return len(nums)


l = [2,3,4,4,3,3,2,2,2]
print(removeElement(l,5))