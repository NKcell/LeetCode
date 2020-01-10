class Solution:
    def topKFrequent(self, nums, k: int):
        from collections import Counter
        res = Counter(nums)
        res1 = sorted(res.items(),key=lambda x:x[1],reverse=True)
        res2 = list()
        for i in range(k):
            res2.append(res1[i][0])
        return res2