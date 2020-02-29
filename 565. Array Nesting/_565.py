class Solution:
    def arrayNesting(self, nums) -> int:
        mySet = set()
        res = list()
        count = 0
        for i,v in enumerate(nums):
            if i in mySet:
                mySet.add(i)
                res.append(count)
                count = 0
                continue
            
            while v not in mySet:
                count+=1
                mySet.add(v)
                v = nums[v]

            res.append(count)
            count = 0

        res.sort()
        return res[-1]

    def arrayNesting1(self, nums):
        seen, res = [0] * len(nums), 0
        for i in nums:
            count, j = 0, i
            while not seen[j]:
                seen[j], count, j = 1, count + 1, nums[j]
            res = max(res, count)
        return res