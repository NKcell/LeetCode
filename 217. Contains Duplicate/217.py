def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return not len(nums) == len(set(nums))

print(containsDuplicate([1,2,3,1]))