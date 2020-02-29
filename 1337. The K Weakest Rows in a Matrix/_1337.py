class Solution:
    def kWeakestRows(self, mat, k: int):
        res = list()
        for i,v in enumerate(mat):
            flag = 0
            for index,value in enumerate(v):
                if value == 0:
                    flag = 1
                    res.append((index,i))
                    break
            if flag == 0:
                res.append((len(mat[0]),i))

        res.sort()
        res2 = list()
        for i in range(k):
            res2.append(res[i][1])
        return res2

    def kWeakestRows1(self, mat, k: int):
        return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]