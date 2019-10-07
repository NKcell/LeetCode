class Solution:
    def searchRange(self, nums, target: int):
        l, r, goal = 0, len(nums)-1, -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                goal = mid
                break
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        
        if goal == -1:
            return [-1,-1]

        l, r = goal, goal
        while l>=0 and nums[l] == target:
            l -= 1
        while r<len(nums) and nums[r] == target:
            r += 1

        return [l+1, r-1]

a = Solution()
print(a.searchRange([1], 1))