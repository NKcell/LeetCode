class Solution:
    def permute(self, nums):
        res = list()
        self.dfs(res, nums, [])
        return res


    def dfs(self, res, nums, tmp):
        if not nums:
            res.append(tmp)

        for i in range(len(nums)):
            self.dfs(res, nums[:i]+nums[i+1:], tmp+[nums[i]])

