class Solution:
    def dominantIndex(self, nums) -> int:
        if len(nums)<2:
            return 0

        if nums[0]>nums[1]:
            a = nums[1]
            b = nums[0]
            index = 0
        else:
            a = nums[0]
            b = nums[1]
            index = 1

        for i in range (2, len(nums)):
            if nums[i]>b:
                a, b = b, nums[i]
                index = i
            elif nums[i]>a:
                a = nums[i]

        if b>=2*a:
            return index
        else:
            return -1