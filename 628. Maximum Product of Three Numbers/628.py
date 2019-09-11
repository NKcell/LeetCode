class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        if nums[-1]<=0:
            return nums[-1]*nums[-2]*nums[-3]
        elif nums[-2]<=0:
            return nums[0]*nums[1]*nums[-1]
        elif nums[-3]<=0:
            return nums[0]*nums[1]*nums[-1]
        else:
            return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

######################################################
# 我的方法整理一下其实可以简化为下面一句
    def maximumProduct1(self, nums) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

# 这个方法可能效率并不是很高，但用堆值得学习借鉴
    def maximumProduct2(self, nums):
        import heapq
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])

# 这个和最开始我想用的方法差不多，只是我一直没有理清真正需要的数，和比较的数
    def maximumProduct3(self, nums):
        max1,max2,max3,min1,min2 = float('-Inf'),float('-Inf'),float('-Inf'),float('Inf'),float('Inf')
        for num in nums:
            if num >= max1:
                max3,max2,max1 = max2,max1,num
            elif num >= max2:
                max3,max2 = max2,num
            elif num > max3:
                max3 = num
            if num <= min1:
                min2,min1 = min1,num
            elif num < min2:
                min2 = num
        return max(max1*max2*max3,min1*min2*max1)

a = Solution()
print(a.maximumProduct([1,2,3,4]))
