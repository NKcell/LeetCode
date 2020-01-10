class Solution:
    def search(self, nums, target: int) -> int:
        start = 0
        end = len(nums)-1

        while start<=end:
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            if target>nums[mid]:
                start = mid+1
            else:
                end = mid-1
        
        return -1