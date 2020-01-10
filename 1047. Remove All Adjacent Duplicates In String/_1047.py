class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = list()
        for i in S:
            if res:
                if res[-1] == i:
                    res = res[:-1]
                else:
                    res.append(i)
            else:
                res.append(i)
        return ''.join(res)