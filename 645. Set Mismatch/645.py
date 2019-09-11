def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    a = sorted(nums)

    for i in range(len(nums)-1):
        if a[i] == a[i+1]:
            fir = a[i]
            a.remove(fir)
            break

    sed = len(nums)
    for i in range(len(nums)-1):
        if a[i] == i+1:
            pass
        else:
            sed = i+1
            break

    return ([fir,sed])

print(findErrorNums([1,5,3,2,2,7,6,4,8,9]))

"""
isum = sum(nums)
tsum = sum(range(len(nums) + 1))
dup = sum(nums) - sum(set(nums))
miss = tsum - isum + dup
return [dup, miss]
"""