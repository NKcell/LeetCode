class Solution:
    def search(self, nums, target: int) -> bool:
        # if not nums:
        #     return False
        
        # if target == nums[-1]:
        #     return True
        
        # start = 0
        # end = len(nums)-1
        # for i in nums:
        #     if i == nums[-1]:
        #         start += 1
        #     else:
        #         break
        # if start>len(nums)-1:
        #     return False
        # truestart = start

        # if nums[start]>nums[end]:
        #     while start <= end:
        #         mid = (start+end)//2
        #         # 中间值比目标值大
        #         if nums[mid]>target:
        #             # 中间值所在区间
        #             # 中间值在第一区间
        #             if nums[mid]>nums[-1]:
        #                 if target>nums[0]:
        #                     if mid>truestart:
        #                         end = mid-1
        #                     else:
        #                         return False
        #                 elif target<nums[0]:
        #                     if mid<len(nums)-1:
        #                         start = mid+1
        #                     else:
        #                         return False
        #                 else:
        #                     return True
        #             # 中间值在第二区间
        #             else:
        #                 if mid>0:
        #                     end = mid-1
        #                 else:
        #                     return False

        #         # 中间值比目标值小
        #         elif nums[mid]<target:
        #             # 中间值所在区间
        #             # 中间值在第二区间
        #             if nums[mid]<=nums[-1]:
        #                 if target>nums[0]:
        #                     if mid>truestart:
        #                         end = mid-1
        #                 elif target<nums[0]:
        #                     if mid<len(nums)-1:
        #                         start = mid+1
        #                 else:
        #                     return True
        #             # 中间值在第一区间
        #             elif nums[mid]>nums[-1]:
        #                 if mid<len(nums)-1:
        #                         start = mid+1
        #                 else:
        #                     return False
        #         else:
        #             return True

        # else:
        #     while start <= end:
        #         mid = (start+end)//2
        #         if nums[mid]<target:
        #             start = mid+1
        #         elif nums[mid]>target:
        #             end = mid-1
        #         else:
        #             return True
        # return False
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            # mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: 
                l += 1

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

a = Solution()
print(a.search( nums = [1,3], target = 3))