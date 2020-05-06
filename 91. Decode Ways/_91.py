class Solution:
    # Time Limit Exceeded
    def numDecodings(self, s: str) -> int:
        s =  [int(i) for i in s]
        res = [0]
        self.dfs(res, s)
        return res[0]
    
    def dfs(self, res, s):
        if len(s) == 0:
            res[0] += 1
            return

        if s[0] == 0:
            return
        
        self.dfs(res, s[1:])

        if len(s)>1:
            tmp = s[0]*10 + s[1]
            if tmp>=1 and tmp<=26:
                self.dfs(res, s[2:])



a = Solution()
print(a.numDecodings("226"))