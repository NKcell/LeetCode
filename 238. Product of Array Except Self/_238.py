class Solution:
    # 这个超时
    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        for i,v in enumerate(nums):
            for index in range(len(nums)):
                if index != i:
                    res[index] *= v
        return res

    def productExceptSelf1(self, nums):
        res = [1]*len(nums)
        tmp = 1
        for i in range(len(nums)):
            res[i] *= tmp
            tmp *= nums[i]

        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]

        return res