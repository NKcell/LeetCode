class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        #  nums[:] = nums[-k:] + nums[:-k] 
        # 这样写明显好很多啊
    
    # 有点意思但不太好理解
    def rotate1(self, nums, k):
        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums)
        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)
    

a = Solution()
nums = [1,2,3,4,5,6]
a.rotate(nums, k = 3)
print(nums)

        
