class Solution:
    def combinationSum3(self, k: int, n: int):
        if n/k > 9 or k>9:
            return []

        res = list()
        for i in range(1, 10):
            tmp = [i]
            self.mysum(n-i, k-1, i, res, tmp)
        return res

    def mysum(self,n,k, minv, res, tmp):
        if k == 0 and n == 0:
            res.append(tmp)
            return
        if k == 0 or n<1:
            return
        for i in range(minv+1, 10):
            self.mysum(n-i, k-1, i, res, tmp+[i])

    def combinationSum3_1(self, k, n):
        from itertools import combinations
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]

        