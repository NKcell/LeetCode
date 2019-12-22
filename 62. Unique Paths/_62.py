class Solution:
    # DP
    def uniquePaths(self, m: int, n: int) -> int:
        res = list()
        for i in range(n):
            res.append([0]*m)
        for i in range(m):
            res[0][i]=1
        for i in range(n):
            res[i][0] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i][j-1]+res[i-1][j]

        return res[-1][-1]

    # dfs 超时...
    def uniquePaths1(self, m: int, n: int) -> int:
        down, right = 0, 0
        res = [0]
        self.dfs(m-1, n-1, down, right, res)
        return res[0]

    def dfs(self, m, n, down, right, res):
        if m == right and n == down:
            res[0]+=1
            return
        if m<right or n<down:
            return
        self.dfs(m, n, down+1, right, res)
        self.dfs(m, n, down, right+1, res)


    # #math C(m+n-2,n-1)
    # def uniquePaths1(self, m, n):
    #     if not m or not n:
    #         return 0
    #     return math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1))
    
    # # O(m*n) space   
    # def uniquePaths2(self, m, n):
    #     if not m or not n:
    #         return 0
    #     dp = [[1 for _ in xrange(n)] for _ in xrange(m)]
    #     for i in xrange(1, m):
    #         for j in xrange(1, n):
    #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #     return dp[-1][-1]

    # # O(n) space 
    # def uniquePaths(self, m, n):
    #     if not m or not n:
    #         return 0
    #     cur = [1] * n
    #     for i in xrange(1, m):
    #         for j in xrange(1, n):
    #             cur[j] += cur[j-1]
    #     return cur[-1]


a = Solution()
print(a.uniquePaths1(2,3))