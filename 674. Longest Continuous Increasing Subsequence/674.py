class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        tmp = 1
        fin = 1
        if not nums:
            return 0
        for index in range(1,len(nums)):
            if nums[index]>nums[index-1]:
                tmp += 1
            else:
                if fin < tmp :
                    fin = tmp
                tmp = 1
        if fin < tmp :
            fin = tmp
        return fin
    
    # DP的思想
    def findLengthOfLCIS1(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

a = Solution()
print(a.findLengthOfLCIS([-1]))