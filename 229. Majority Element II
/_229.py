class Solution:
    def majorityElement(self, nums):
        if not nums:
            return nums
        nums.sort()
        res = list()
        i = 0
        l = len(nums)//3
        while i<=(2*l+1):
            if len(nums)<=i+l:
                break
            if nums[i] == nums[i+l]:
                res.append(nums[i])
                i = i+l+1
            else:
                i+=1

        return list(set(res))

    def majorityElement1(self, nums):
        import collections
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums)/3]