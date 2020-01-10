class Solution:
    def sumZero(self, n: int) :
        res = list()
        if n%2 == 1:
            n -= 1
            res.append(0)
        
        while n != 0:
            res.append(n)
            res.append(-n)
            n -= 2

        return res 