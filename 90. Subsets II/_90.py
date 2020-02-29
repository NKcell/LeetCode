class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = list()
        res.append([])

        tmp = ""
        last = res[-1]
        for index, value in enumerate(nums):
            if tmp == value:
                continue
            res.append(last+[value])
            self.dfs(res, nums[index+1:])
            tmp = value

        return res

    def dfs(self, res, nums): 
        tmp = ""
        last = res[-1]
        for index, value in enumerate(nums):
            if tmp == value:
                continue
            res.append(last+[value])
            self.dfs(res, nums[index+1:])
            tmp = value

    def subsetsWithDup1(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res