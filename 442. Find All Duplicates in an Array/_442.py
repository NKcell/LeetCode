class Solution:
    def findDuplicates(self, nums):
        nums.sort()
        res = list()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])

        return res

    def findDuplicates1(self, nums):
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res