class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        r = l = mysum = 0
        res = len(nums)+1
        while r<len(nums) or mysum>=s:
            if mysum<s:
                mysum += nums[r]
                r += 1
            else:
                res = min(res, r-l)
                mysum -= nums[l]
                l += 1

        if res<=len(nums):
            return res
        return 0