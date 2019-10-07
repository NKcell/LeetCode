class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        fin = nums[r]

        if target == fin:
            return r

        mid = -1
        if nums[0]>nums[-1]:

            # 这里的二分法要注意取等！
            while l<=r:
                mid = (l+r)//2
                if nums[mid]>fin and nums[mid+1]<nums[mid]:
                    break
                elif nums[mid]>fin:
                    l = mid+1
                else:
                    r = mid - 1

            if mid == -1:
                return -1
            if target > fin:
                l, r = 0, mid
            else:
                l, r = mid+1, len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return -1

    # 这也是二分法，但明显思考问题思考的更透彻，
    def search1(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    def search2(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo if target in nums[lo:lo+1] else -1

a = Solution()
print(a.search(nums = [5, 1, 3], target = 1))