class Solution:
    def checkPossibility(self, nums):
        flag = 0
        for i in range(len(nums)-1):

            if nums[i]>nums[i+1]:
                if i != 0:
                    if nums[i+1]<nums[i-1]:
                        nums[i+1] = nums[i]
                flag += 1

            if flag > 1:
                return False

        return True

    ###########################################
    # 这个想法还是很有意思的，关键的就是在一次去除之后，就能成递增
    # 两个数，去除其中一个，这里就新建两个列表，代表两种可能，然后再对两个列表排序，如果ok，那至少其中一个列表在排序后无序列变化
    # 但这种做法内存和时间都不会表现很好
    def checkPossibility1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)
    
    ###########################################
    # 这个优秀的地方在于尽量的把判断放在了循环外面，然后在列表的头和尾添加了无穷大和无穷小，减少了判断
    def checkPossibility2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [float("-inf")] + nums + [float("inf")]
        count = 0
        for i in range(1, len(nums)-1):   
            if nums[i] > nums[i+1]:
                index = i
                count += 1
                if count == 2:
                    return False     
        if count == 0: return True
        if count == 1 and nums[index-1]<= nums[index+1]: return True
        if count == 1 and nums[index] <= nums[index+2]: return True                   
        return False

a = Solution()
print(a.checkPossibility([2,3,3,2,4]))

"""
float("-inf")   无穷小
float("inf")    无穷大
"""