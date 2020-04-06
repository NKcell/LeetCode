class Solution:
    def generateParenthesis(self, n: int):
        res = list()
        
        if n == 0:
            return res
        
        l = 0
        r = n
        self.dfs(res, "", r, l, 2*n)

        return res


    def dfs(self, res, tmpstr, r, l, n):
        if len(tmpstr) == n:
            res.append(tmpstr)

        if r != 0:
            self.dfs(res, tmpstr+'(', r-1, l+1, n)
        if l != 0:
            self.dfs(res, tmpstr+')', r, l-1, n)


a = Solution()
print(a.generateParenthesis(3))