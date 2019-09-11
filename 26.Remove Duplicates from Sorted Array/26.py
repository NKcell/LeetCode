def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums == []:
        return 0

    needdel = []
    flag = 0
    for i in range(len(nums)):
        if nums[i] == nums[flag]:
            needdel.append(i)
        else:
            flag = i

    needdel.pop(0)

    if needdel is not None:
        flag = 0
        for i in needdel:
            nums.pop(i-flag)
            flag += 1

    return len(nums)


print(removeDuplicates([]))








