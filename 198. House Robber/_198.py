class Solution:
    def rob(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        first = nums[0]
        second = max(first, nums[1])

        for i in range(2, len(nums)):
            if  nums[i]+first>second:
                first, second = second, nums[i]+first
            else:
                first = second
        
        return second

    # 动态规划的思想
    # 这个写的简洁很多，少了判断
    # 在写go的时候，有反应减少判断，但依旧没有这个减少的好
    def rob1(self, nums):
            last, now = 0, 0
            for i in nums: last, now = now, max(last + i, now)
            return now