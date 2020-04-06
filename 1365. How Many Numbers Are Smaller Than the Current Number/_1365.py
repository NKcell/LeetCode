class Solution:
    def smallerNumbersThanCurrent(self, nums):
        myDict = dict()
        nums2 = sorted(nums)
        for i,v in enumerate(nums2):
            tmp = myDict.get(v, -1)
            if tmp == -1:
                myDict[v] = i

        res = list()
        for i in nums:
            res.append(myDict[i])

        return res

a = Solution()
print(a.smallerNumbersThanCurrent([7,7,7,7]))
