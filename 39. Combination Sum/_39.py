class Solution:
    # dfs
    def combinationSum(self, candidates, target: int):
        candidates.sort()
        res = []
        self.findSum(candidates, target, res, [])
        return res
        
    def findSum(self, candidates, target, res, tmp):
        if target<0:
            return
        if target == 0:
            res.append(tmp)
            return
        for i in range(len(candidates)):
            if target-candidates[i] < 0:
                break
            self.findSum(candidates[i:], target-candidates[i], res, tmp+[candidates[i]])

    # dp
    def combinationSum1(self, nums, target: int) -> int:
        # 保存方案，使用三维数组
        # 第一维： dp:List 表示和为不同数时的方案
        # 第二维： dp[s]:List 表示和i的方案列表
        # 第三维 每种具体的方案都是数组， dp[s][j]:List 表示和为s的第j个方案的数组
        dp: list = [[[]]] + [[] for i in range(target)]  # 初始化 eg: [[[]], [], [], [], [], []]， 保证和为0有一种方案 [], 完全背包需要恰好装满的时候，dp[0] 必须初始化为0

        for n in nums:  # 对于每个数
            for s in range(n, target + 1):  # 完全背包，从小到大
                li = [l + [n] for l in dp[s - n]]  # 对于把和为s-n的每种方案，添加数字n, 就变成一种新的 和为s的方案
                dp[s] += li  # 把新方案添加到 原来和为s的方案里
        return dp[target]

# a = Solution()
# print(a.combinationSum([2,3,5], 8))