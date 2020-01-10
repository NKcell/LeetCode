class Solution:
    def calPoints(self, ops) -> int:
        res = [0,0]
        for i in ops:
            if i == 'D':
                res.append(res[-1]*2)
            elif i == '+':
                res.append(res[-1]+res[-2])
            elif i == 'C':
                if len(res)>2:
                    res.pop()
            else:
                res.append(int(i))

        return sum(res)