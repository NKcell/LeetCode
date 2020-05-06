class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = list()
        nums = list(range(1, n+1))
        self.dfs(k, res, [], nums)
        return res

    def dfs(self, n, res, tmp, nums):
        if n == 0:
            res.append(tmp)
        
        if len(nums)<n:
            return

        for i,v in enumerate(nums):
            if len(nums)-i < n:
                break
            
            self.dfs(n-1, res, tmp+[v], nums[i+1:])

