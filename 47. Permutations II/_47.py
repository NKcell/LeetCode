class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, tmp):
        if len(nums) == 0:
            res.append(tmp)
            return
        for i in range(len(nums)):
            if i == 0:
                pre = nums[0]
                self.dfs(nums[1:], res, tmp+[nums[0]])

            else:
                if nums[i] == pre:
                    continue

                else:
                    pre = nums[i]
                    self.dfs(nums[:i]+nums[i+1:], res, tmp+[nums[i]])

