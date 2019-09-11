"""
581. Shortest Unsorted Continuous Subarray
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""

"""
def findUnsortedSubarray(nums):
   
    sort_nums = sorted(nums)

    pre = 0
    while True:
        if pre < len(nums) and nums[pre] == sort_nums[pre]:
            pre += 1
        else:
            break

    if pre == len(nums) :
        return 0

    fin = len(nums) - 1
    while True:
        if nums[fin] == sort_nums[fin] and fin != pre:
            fin -= 1
        else:
            break

    return fin - pre + 1


print(findUnsortedSubarray([2,3,4]))
"""

"""
def findUnsortedSubarray(nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
"""





def findUnsortedSubarray(nums):
    n = len(nums)
    cmax, cmin = -float('inf'), float('inf')
    l, r = 0, -1
    for i in range(n):
        cmax = max(cmax, nums[i])
        cmin = min(cmin, nums[n - 1 - i])
        if nums[i] != cmax: r = i
        if nums[n - 1 - i] != cmin: l = n - 1 - i

    print(r)
    print(l)
    return r - l + 1
print(findUnsortedSubarray([1, 2, 8, 3, 4, 6]))