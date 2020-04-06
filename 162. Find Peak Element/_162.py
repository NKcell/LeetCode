class Solution:
    def findPeakElement(self, nums) -> int:
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if nums[0]>nums[-1]:
            return 0
        return len(nums)-1

    def findPeakElement2(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l 