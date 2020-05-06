class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = list()
        tmp = list()
        self.dfs(res, tmp, s)
        return res

    def dfs(self, res, tmp, s):
        if len(s) == 0:
            res.append(tmp)
            return

        for i,v in enumerate(s):
            if self.ispar(s[:i+1]):
                self.dfs(res, tmp+[s[:i+1]], s[i+1:])


    def ispar(self, s):
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1
        return True 