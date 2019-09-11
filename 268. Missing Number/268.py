class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
    
    # 超时我也是醉了
    def missingNumber1(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)-1,i,-1):
                if nums[j]<nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
            if nums[i] != i:
                return i
        return len(nums)

    # 这个算法是深入理解题目了的，进行分析，空间和时间都是完美
    def missingNumber2(self, nums):
        n = len(nums)
        return n * (n+1) / 2 - sum(nums)\
        
    # 还有一种异或的方法，遍历一遍进行异或，出现两次的为0，出现一次的剩在了最后

a = Solution()
print(a.missingNumber1([0]))