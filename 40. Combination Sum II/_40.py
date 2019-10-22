class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        
        def findNum(nums, target, res, tmp):
            for i, v in enumerate(nums):
                # 重要的就是这里去重
                if i!=0 and v == nums[i-1]:
                    continue
                if target == v:
                    res+=[tmp+[v]]
                    return
                elif target > v:
                    findNum(nums[i+1:], target-v, res, tmp+[v])
                else:
                    return
        
        res = list()
        findNum(candidates, target, res, [])
        return res

    # dp的方法
    def combinationSum2_1(self, candidates, target):
        candidates.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])