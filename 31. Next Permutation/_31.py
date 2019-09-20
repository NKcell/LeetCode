# 这里主要是要理解字典序算法
# 最后我用的是冒泡排序来实现的交换后的排列，但仔细一想就可以发现
# 根据字典序的特征用反转是最合适的做法

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loc = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                loc = i-1
                break

        if loc == -1:
            nums.sort()
        else:
            for i in range(len(nums)-1, loc, -1):
                if nums[i]>nums[loc]:
                    nums[i], nums[loc] = nums[loc], nums[i]
                    break
            for i in range(loc+1, len(nums)-1):
                for j in range(len(nums)-1, i, -1):
                    if nums[j]<nums[j-1]:
                        nums[j], nums[j-1] = nums[j-1], nums[j]

    def nextPermutation1(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    寻找基于字典序的下一个排列。   
    """
        l = len(nums)
        
        # 从右向左查询第一个小于右邻的元素
        for i in range(l-2, -1, -1):
            if nums[i+1] > nums[i]:
                break
        else: # 没有找到，说明为降序排列
            nums[:] = nums[::-1]
            return
        
        # 从右向左查询第一个大于nums[i]的元素
        for j in range(l-1, -1, -1):
            if nums[j] > nums[i]:
                break
        
        # 交换i和j
        nums[i], nums[j] = nums[j], nums[i]            
        
        # i后面的序列进行反转
        nums[i+1:l] = nums[-1:i:-1]



