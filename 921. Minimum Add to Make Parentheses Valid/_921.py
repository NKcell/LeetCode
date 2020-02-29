class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = list()
        for i in S:
            if i == '(':
                res.append('(')
            else:
                if len(res) == 0:
                    res.append(')')
                elif res[-1] == '(':
                    res.pop()
                else:
                    res.append(')')
        return len(res)