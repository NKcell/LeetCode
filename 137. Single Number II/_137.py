class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)<3:
            return nums[0]
        nums.sort()
        i = 0
        while i<len(nums):
            if i+2>=len(nums):
                return nums[i]
            if nums[i] != nums[i+2]:
                return nums[i]

            i += 3