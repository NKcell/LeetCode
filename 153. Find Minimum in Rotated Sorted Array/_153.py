class Solution:
    def findMin(self, nums) -> int:
        if nums[-1]>=nums[0]:
            return nums[0]

        r = len(nums)-1
        l = 0

        while l<=r:
            mid = (r-l)//2 + l

            if mid == 0:
                l = mid + 1
                continue
            if mid == len(nums)-1:
                return nums[-1]

            if nums[mid]<nums[mid+1] and nums[mid]<nums[mid-1]:
                return nums[mid]

            if nums[mid]>nums[0]:
                l = mid+1
            else:
                r = mid-1
        
        return nums[0]

    def findMin1(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))