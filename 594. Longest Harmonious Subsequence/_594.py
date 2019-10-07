class Solution:
    def findLHS(self, nums) -> int:
        mydict = {}
        for i in nums:
            v = mydict.get(i, 0)
            mydict[i] = v+1
        nums = list(set(nums))
        nums.sort()
        maxvalue = 0
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 1:
                tmp = abs(mydict[nums[i]]+mydict[nums[i-1]])
                if maxvalue<tmp:
                    maxvalue = tmp
        return maxvalue

    # 这个和上面的效率差不多， 这个查找还是很多的
    def findLHS1(self, nums):
        import collections
        c = collections.Counter(nums)
        return max([c[x] + c[x + 1] for x in c if x + 1 in c] or [0])