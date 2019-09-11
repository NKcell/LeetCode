class Solution:
    def pivotIndex(self, nums) -> int:
        if len(nums) == 0:
            return -1
        total = sum(nums)
        tmp = 0
        if total - nums[0] == 0:
            return 0
        for index,value in enumerate(nums):
            if index+1 >= len(nums):
                if total - nums[-1] == 0:
                    return len(nums)-1
                else:
                    return -1
            tmp += value
            if tmp == (total-(nums[index+1]))/2:
                return index+1

    # 思想是一样的，但这个控制临界点好很多    
    def pivotIndex1(self, nums):
        # Time: O(n)
        # Space: O(1)
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
    
    # 思想一样，但这个乘法操作很闪光
    def pivotIndex2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        sum_so_far = 0
        for i in range(len(nums)):
            if sum_so_far * 2 + nums[i] == total_sum:
                return i
            else:
                sum_so_far += nums[i]
        return -1

a = Solution()
print(a.pivotIndex([-1,-1,1,1,0,0]))